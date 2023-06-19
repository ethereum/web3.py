import json
import os
from enum import (
    Enum,
)
from typing import (
    List,
    Optional,
    Set,
    Union,
)

from pyunormalize import (
    NFC,
    NFD,
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
    for e in NORMALIZATION_SPEC["emoji"]:
        if 65039 in e:
            for i in range(e.count(65039)):
                e.remove(65039)

with open(os.path.join(specs_dir_path, "nf.json")) as nf:
    NF = _json_list_mapping_to_dict(nf, "decomp")


# --- Classes -- #


class Token:
    type: str
    _original_text: str
    _original_codepoints: List[int]
    _normalized_codepoints: Optional[List[int]] = None

    restricted: bool = False

    def __init__(self, original_text: str, original_codepoints: List[int]) -> None:
        self._raw_text = original_text
        self._original_codepoints = original_codepoints

    @property
    def codepoints(self) -> List[int]:
        return (
            self._normalized_codepoints
            if self._normalized_codepoints
            else self._original_codepoints
        )

    @property
    def text(self) -> str:
        return _cps_to_text(self.codepoints)


class TokenType(Enum):
    EMOJI = "emoji"
    TEXT = "text"


class EmojiToken(Token):
    type: TokenType.EMOJI = TokenType.EMOJI


class TextToken(Token):
    type: TokenType.TEXT = TokenType.TEXT


class Label:
    type: str
    tokens: List[Union[TextToken, EmojiToken]]

    def __init__(
        self,
        type: str = None,
        tokens: List[Union[TextToken, EmojiToken]] = None,
    ) -> None:
        self.type = type
        self.tokens = tokens

    @property
    def text(self) -> str:
        if not self.tokens:
            return ""

        return "".join(token.text for token in self.tokens)


class ENSNormalizedName:
    labels: List[Label]

    def __init__(self, normalized_labels: List[Label]) -> None:
        self.labels = normalized_labels

    @property
    def as_text(self) -> str:
        return ".".join(label.text for label in self.labels)


# -----

GROUP_COMBINED_VALID_CPS = []
for d in NORMALIZATION_SPEC["groups"]:
    GROUP_COMBINED_VALID_CPS.extend(d["primary"])
    GROUP_COMBINED_VALID_CPS.extend(d["secondary"])

VALID_BY_GROUPS = {
    d["name"]: set(d["primary"] + d["secondary"]) for d in NORMALIZATION_SPEC["groups"]
}


def _extract_valid_codepoints() -> Set[int]:
    all_valid = set()
    for _name, valid_cps in VALID_BY_GROUPS.items():
        all_valid.update(valid_cps)
    all_valid.update(map(ord, NFD("".join(map(chr, all_valid)))))
    return all_valid


def _construct_whole_confusable_map():
    whole_map = {}
    for whole in NORMALIZATION_SPEC["wholes"]:
        whole_confusables = set(whole["valid"] + whole["confused"])
        confusable_extents = []

        for confusable_cp in whole_confusables:
            # create confusable extents for all whole confusables
            groups = set()
            for gn, gv in VALID_BY_GROUPS.items():
                if confusable_cp in gv:
                    groups.add(gn)

            if len(confusable_extents) == 0:
                confusable_extents.append([[confusable_cp], groups])
            else:
                extent_exists = False
                for entry in confusable_extents:
                    if any(g in entry[1] for g in groups):
                        extent_exists = True
                        entry[0].append(confusable_cp)
                        entry[1].update(groups)
                        break

                if not extent_exists:
                    confusable_extents.append([[confusable_cp], groups])

        for confusable_cp in whole_confusables:
            confusable_cp_extent_groups = set()

            if confusable_cp in whole["confused"]:
                whole_map[confusable_cp] = set()
                for ce in confusable_extents:
                    if confusable_cp in ce[0]:
                        confusable_cp_extent_groups.update(ce[1])
                    else:
                        whole_map[confusable_cp].update(ce[1])

                # remove the groups from confusable_cp's confusable extent
                whole_map[confusable_cp] = whole_map[confusable_cp].difference(
                    confusable_cp_extent_groups
                )

    return whole_map


WHOLE_CONFUSABLE_MAP = _construct_whole_confusable_map()
VALID_CODEPOINTS = _extract_valid_codepoints()
MAX_LEN_EMOJI_PATTERN = max(len(e) for e in NORMALIZATION_SPEC["emoji"])
WHOLE_CONFUSABLES = NORMALIZATION_SPEC["wholes"]
NSM_MAX = NORMALIZATION_SPEC["nsm_max"]


def _is_fenced(cp: int) -> bool:
    return cp in [fenced[0] for fenced in NORMALIZATION_SPEC["fenced"]]


def _cps_to_text(cps: List[Union[int, List[int]]]) -> str:
    return "".join(chr(cp) if isinstance(cp, int) else _cps_to_text(cp) for cp in cps)


def validate_tokens_and_get_label_type(tokens: List[Token]) -> str:
    """
    Validate tokens and return the label type.

    :param List[Token] tokens: the tokens to validate
    :raises InvalidName: if the tokens are invalid
    """

    if all(token.type == TokenType.EMOJI for token in tokens):
        return "emoji"

    label_text = "".join(token.text for token in tokens)
    concat_text_tokens_as_str = "".join(
        t.text for t in tokens if t.type == TokenType.TEXT
    )
    all_token_cps = [cp for t in tokens for cp in t.codepoints]

    if len(tokens) == 1 and tokens[0].type == TokenType.TEXT:
        # if single text token
        encoded = concat_text_tokens_as_str.encode()
        try:
            encoded.decode("ascii")  # if label is ascii

            if "_" in concat_text_tokens_as_str[concat_text_tokens_as_str.count("_") :]:
                raise InvalidName(
                    "Underscores '_' may only occur at the start of a label: "
                    f"{label_text}"
                )
            elif concat_text_tokens_as_str[2:4] == "--":
                raise InvalidName(
                    "A label's third and fourth characters cannot be hyphens '-': "
                    f"{label_text}"
                )
            return "ascii"
        except UnicodeDecodeError:
            pass

    if 95 in all_token_cps[all_token_cps.count(95) :]:
        raise InvalidName(
            f"Underscores '_' may only occur at the start of a label: {label_text}"
        )

    if _is_fenced(all_token_cps[0]) or _is_fenced(all_token_cps[-1]):
        raise InvalidName(
            f"Label cannot start or end with a fenced codepoint: {label_text}"
        )

    for cp_index, cp in enumerate(all_token_cps):
        if cp_index == len(all_token_cps) - 1:
            break
        next_cp = all_token_cps[cp_index + 1]
        if _is_fenced(cp) and _is_fenced(next_cp):
            raise InvalidName(
                f"Label cannot contain two fenced codepoints in a row: {label_text}"
            )

    if any(
        t.codepoints[0] in NORMALIZATION_SPEC["cm"]
        for t in tokens
        if t.type == TokenType.TEXT
    ):
        raise InvalidName(
            "At least one text token in label starts with a "
            f"combining mark: {label_text}"
        )

    # find first group that contains all chars in label
    text_token_cps_set = {
        cp
        for token in tokens
        if token.type == TokenType.TEXT
        for cp in token.codepoints
    }
    chars_group_name = None
    for group_name, group_cps in VALID_BY_GROUPS.items():
        if text_token_cps_set.issubset(group_cps):
            chars_group_name = group_name
            break

    if not chars_group_name:
        raise InvalidName(
            f"Label contains codepoints from multiple groups - label: {label_text}"
        )

    # apply NFD and check contiguous NSM sequences
    for group in NORMALIZATION_SPEC["groups"]:
        if group["name"] == chars_group_name and "cm" not in group:
            nfd_cps = [
                ord(nfd_c) for c in concat_text_tokens_as_str for nfd_c in NFD(c)
            ]

            next_index = -1
            for cp_i, cp in enumerate(nfd_cps):
                if cp_i <= next_index:
                    continue

                if cp in NORMALIZATION_SPEC["nsm"]:
                    if cp_i == len(nfd_cps) - 1:
                        break

                    contiguous_nsm_cps = [cp]
                    next_index = cp_i + 1
                    next_cp = nfd_cps[next_index]
                    while next_cp in NORMALIZATION_SPEC["nsm"]:
                        contiguous_nsm_cps.append(next_cp)
                        if len(contiguous_nsm_cps) > NSM_MAX:
                            raise InvalidName(
                                "Contiguous NSM sequence for label is beyond nsm "
                                f"max of {NSM_MAX}: {label_text}"
                            )
                        next_index += 1
                        if next_index == len(nfd_cps):
                            break
                        next_cp = nfd_cps[next_index]

                    if not len(contiguous_nsm_cps) == len(set(contiguous_nsm_cps)):
                        raise InvalidName(
                            "Contiguous NSM sequence for label contains duplicate "
                            f"codepoints: {label_text}"
                        )

    # check wholes
    # start with set of all groups with confusables
    retained_groups = set(VALID_BY_GROUPS.keys())
    confused_chars = set()
    buffer = set()

    for char_cp in text_token_cps_set:
        groups_excluding_ce = WHOLE_CONFUSABLE_MAP.get(char_cp)

        if groups_excluding_ce and len(groups_excluding_ce) > 0:
            if len(retained_groups) == 0:
                break
            else:
                retained_groups = retained_groups.intersection(groups_excluding_ce)
                confused_chars.add(char_cp)

        elif GROUP_COMBINED_VALID_CPS.count(char_cp) == 1:
            return chars_group_name

        else:
            buffer.add(char_cp)

    if len(confused_chars) > 0:
        for retained_group_name in retained_groups:
            if all(cp in VALID_BY_GROUPS[retained_group_name] for cp in buffer):
                # Though the spec doesn't mention this explicitly, if the buffer is
                # empty, the label is confusable. This allows for using ``all()`` here
                # since that yields ``True`` on empty sets.
                # e.g. ``all(cp in group_cps for cp in set())`` is ``True``
                # for any ``group_cps``.
                raise InvalidName(
                    f"Label is confusable: {concat_text_tokens_as_str} "
                    f"({chars_group_name} / {retained_group_name})"
                )

    return chars_group_name


def _build_and_validate_label_from_tokens(tokens: List[Token]) -> Label:
    for token in tokens:
        if token.type == TokenType.TEXT:
            # apply NFC normalization to text tokens
            chars = [chr(cp) for cp in token._original_codepoints]
            nfc = NFC(chars)
            token._normalized_codepoints = [ord(c) for c in nfc]

    label_type = validate_tokens_and_get_label_type(tokens)

    label = Label()
    label.type = label_type
    label.tokens = tokens
    return label


def normalize_name_ensip15(name: str) -> ENSNormalizedName:
    """
    Normalize an ENS name according to ENSIP-15
    https://docs.ens.domains/ens-improvement-proposals/ensip-15-normalization-standard

    :param str name: the dot-separated ENS name
    :raises InvalidName: if ``name`` has invalid syntax
    """

    if not name:
        raise InvalidName("Name cannot be empty")
    elif isinstance(name, (bytes, bytearray)):
        name = name.decode("utf-8")

    raw_labels = name.split(".")

    if any(len(label) == 0 for label in raw_labels):
        raise InvalidName("Labels cannot be empty")

    normalized_labels = []

    for label_str in raw_labels:
        # _input takes the label and breaks it into a list of unicode code points
        # e.g. "xyz👨🏻" -> [120, 121, 122, 128104, 127995]
        _input = [ord(c) for c in label_str]
        buffer = []
        tokens = []

        while len(_input) > 0:
            emoji_codepoint = None
            end_index = 1
            while end_index <= len(_input):
                current_emoji_sequence = _input[:end_index]

                if len(current_emoji_sequence) > MAX_LEN_EMOJI_PATTERN:
                    # if we've reached the max length of all known emoji patterns
                    break

                # remove 0xFE0F (65039)
                elif 65039 in current_emoji_sequence:
                    current_emoji_sequence.remove(65039)
                    _input.remove(65039)
                    end_index -= 1  # reset end_index after removing 0xFE0F

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
                    mapped = NORMALIZATION_SPEC["mapped"][leading_codepoint]
                    for cp in mapped:
                        buffer.append(cp)

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
        normalized_label = _build_and_validate_label_from_tokens(tokens)
        normalized_labels.append(normalized_label)

    # - Join raw_labels back together
    return ENSNormalizedName(normalized_labels)


def _buffer_codepoints_to_chars(buffer):
    return "".join(
        "".join(chr(c) for c in char) if isinstance(char, list) else chr(char)
        for char in buffer
    )
