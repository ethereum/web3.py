import itertools
import json
import os
from typing import (
    List,
    Set,
    Union,
)

from ens.exceptions import InvalidName


def _json_list_mapping_to_dict(json_file, list_mapped_key: str):
    """
    Takes a `[key, [value]]` mapping from the original ENS spec json files and turns it
    into a `{key: value}` mapping.
    """
    f = json.load(json_file)
    f[list_mapped_key] = {k: v for k, v in f[list_mapped_key]}
    return f


# get the normalization spec json files downloaded from links in ENSIP-15
# https://docs.ens.domains/ens-improvement-proposals/ensip-15-normalization-standard
specs_dir_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "specs"))
with open(os.path.join(specs_dir_path, "normalization_spec.json")) as spec:
    NORMALIZATION_SPEC = _json_list_mapping_to_dict(spec, "mapped")
    # clean `FE0F` (65039) from entries since it's optional
    [e.remove(65039) for e in NORMALIZATION_SPEC["emoji"] if 65039 in e]

with open(os.path.join(specs_dir_path, "nf.json")) as nf:
    NF = _json_list_mapping_to_dict(nf, "decomp")


# --- Classes -- #


class Token:
    text: str
    codepoints: List[int]
    restricted: bool = False

    def __init__(self, text: str, codepoints: List[int]) -> None:
        self.text = text
        self.codepoints = codepoints


class EmojiToken(Token):
    type = "emoji"


class TextToken(Token):
    type = "text"


class Label:
    type: str
    nfc: List[int]
    nfc_text: str
    tokens: List[Union[TextToken, EmojiToken]]

    def __init__(self) -> None:
        self.tokens = []
        self.nfc = []

    @property
    def text(self) -> str:
        return "".join([token.text for token in self.tokens])


# -----


def _extract_valid_codepoints() -> Set[int]:
    valid = set()
    for group in NORMALIZATION_SPEC["groups"]:
        valid_codepoints = set(group["primary"] + group["secondary"])
        valid.update(valid_codepoints)
        valid.add(
            NF["decomp"][codepoint]
            for codepoint in valid_codepoints
            if codepoint in NF["decomp"]
        )
    valid.update(NORMALIZATION_SPEC["cm"])
    return valid


VALID_CODEPOINTS = _extract_valid_codepoints()


def process_and_validate_label_from_tokens(tokens: List[Token]) -> Label:
    # TODO: validate tokenized_label
    label = Label()
    label.tokens = tokens
    return label


def normalize_name_ensip15(name: str) -> str:
    """
    Normalize an ENS name according to ENSIP-15
    https://docs.ens.domains/ens-improvement-proposals/ensip-15-normalization-standard

    :param str name: the dot-separated ENS name
    :raises InvalidName: if ``name`` has invalid syntax
    """

    if not name:
        return name
    elif isinstance(name, (bytes, bytearray)):
        name = name.decode("utf-8")

    # trim whitespace / strip name
    stripped_name = name.strip()
    raw_labels = stripped_name.split(".")
    normalized_labels = []

    for label_str in raw_labels:
        # _input takes the label and breaks it into a list of unicode code points
        # e.g. "xyz👨🏻" -> [120, 121, 122, 128104, 127995]
        _input = list(itertools.chain(*([ord(c) for c in char] for char in label_str)))
        buffer = []
        tokens = []

        while len(_input) > 0:
            emoji_codepoint = None
            end_index = 1
            while end_index <= len(_input):
                current_emoji_sequence = _input[:end_index]
                if 65039 in current_emoji_sequence:
                    current_emoji_sequence.remove(65039)
                if current_emoji_sequence in NORMALIZATION_SPEC["emoji"]:
                    emoji_codepoint = current_emoji_sequence
                end_index += 1

            if emoji_codepoint:
                if len(buffer) > 0:
                    # emit `Text` token with values in buffer
                    chars = _buffer_codepoints_to_chars(buffer)
                    tokens.append(TextToken(chars, buffer))
                    buffer = []  # clear the buffer

                # emit `Emoji` token with values in emoji_codepoint
                emoji_text = "".join([chr(codepoint) for codepoint in emoji_codepoint])
                tokens.append(EmojiToken(emoji_text, emoji_codepoint))
                _input = _input[len(emoji_codepoint) :]

            else:
                leading_codepoint = _input.pop(0)

                if leading_codepoint in NORMALIZATION_SPEC["ignored"]:
                    pass

                elif leading_codepoint in NORMALIZATION_SPEC["mapped"]:
                    buffer.append(NORMALIZATION_SPEC["mapped"][leading_codepoint])

                else:
                    if leading_codepoint in VALID_CODEPOINTS:
                        buffer.append(leading_codepoint)
                    else:
                        raise InvalidName(
                            f"Invalid codepoint: {leading_codepoint} "
                            f"({hex(leading_codepoint)})"
                        )

            if len(buffer) > 0 and len(_input) == 0:
                chars = _buffer_codepoints_to_chars(buffer)
                tokens.append(TextToken(chars, buffer))

        # create a `Label` instance from tokens
        # - Apply NFC to each `Text` token
        # - Run tokens through "Validation" section of ENSIP-15
        normalized_label = process_and_validate_label_from_tokens(tokens)
        normalized_labels.append(normalized_label.text)

    # - Join raw_labels back together
    return ".".join(normalized_labels)


def _buffer_codepoints_to_chars(buffer):
    return "".join(
        [
            "".join([chr(c) for c in char]) if isinstance(char, list) else chr(char)
            for char in buffer
        ]
    )
