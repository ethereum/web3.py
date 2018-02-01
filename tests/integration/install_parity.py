import hashlib
import os
import stat

from eth_utils import (
    to_tuple,
)
import requests
import toolz

URI_QUERY_URL = "https://vanity-service.parity.io/parity-binaries"
BASE_BIN_PATH = "~/.parity-bin"
VERSION_STRINGS = {
    "v1.8.7": "1_8_7",
    "v1.8.8": "1_8_8",
    "v1.9.1": "1_9_1"
}
ARCHITECTURE = 'x86_64'
OS = 'linux'


@toolz.curry
def fill_default_request_params(version, os=OS, architecture=ARCHITECTURE):
    params = {'version': version, 'os': os, 'architecture': architecture}
    return params


@toolz.functoolz.memoize
def get_parity_release_json(**kwargs):
    return requests.get(
        URI_QUERY_URL,
        params=kwargs).json()


@to_tuple
def get_binary_uri(releases_json):
    for release in releases_json:
        binary_uri = ((uri.get('downloadUrl', None), uri.get('checksum', None))
                      for uri in release.get('files', tuple())
                      if uri.get('name') == 'parity')
        yield next(binary_uri)


def get_executable_path(version_string):
    identifier = VERSION_STRINGS[version_string]
    path = os.path.join(BASE_BIN_PATH, 'parity-{0}'.format(identifier))
    return os.path.expanduser(path)


def install_parity(version_string):
    if version_string not in VERSION_STRINGS.keys():
        raise ValueError("{0} is not an accepted version identifier.")

    path = get_executable_path(version_string)

    get_uri = toolz.functoolz.compose(
        get_binary_uri,
        get_parity_release_json)
    params = fill_default_request_params(version_string)
    uri, checksum = get_uri(**params)[0]

    if not os.path.exists(path):
        download_binary(path, uri, checksum)

    return path


def download_binary(path, uri, checksum):
    bin_stream = get_binary_stream(uri)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    digest = hashlib.md5()
    with open(path, 'wb') as f:
        for chunk in bin_stream:
            f.write(chunk)
            digest.update(chunk)
    assert digest.hexdigest() == checksum
    chmod_plus_x(path)


def chmod_plus_x(executable_path):
    current_st = os.stat(executable_path)
    os.chmod(executable_path, current_st.st_mode | stat.S_IEXEC)


def get_binary_stream(uri):
    resp = requests.get(uri, stream=True)
    if resp.status_code == 200:
        return resp.raw
    else:
        resp.raise_for_status()
