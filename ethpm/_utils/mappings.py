import itertools
from typing import Any, Dict, Iterable, Tuple

from eth_utils import is_dict, to_dict


@to_dict
def deep_merge_dicts(*dicts: Dict[Any, Any]) -> Iterable[Tuple[Any, Any]]:
    for key in set(itertools.chain(*(_dict.keys() for _dict in dicts))):
        values = tuple((_dict[key] for _dict in dicts if key in _dict))
        if is_dict(values[-1]):
            yield key, deep_merge_dicts(
                *(_dict[key] for _dict in dicts if is_dict(_dict.get(key)))
            )
        else:
            yield key, values[-1]
