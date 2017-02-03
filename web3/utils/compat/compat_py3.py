import collections

from urllib.parse import (  # noqa: F401
    urlparse,
    urlunparse,
)

try:
    Generator = collections.Generator
except AttributeError:
    # py34
    Generator = type(_ for _ in tuple())
