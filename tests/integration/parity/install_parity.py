import hashlib
from json.decoder import (
    JSONDecodeError,
)
import os
import stat
import sys

from eth_utils import (
    to_tuple,
)
import requests
import toolz
from tqdm import tqdm

URI_QUERY_URL = "https://vanity-service.parity.io/parity-binaries"
BASE_BIN_PATH = "~/.parity-bin"
VERSION_STRINGS = {
    "v1.8.7": "1_8_7",
    "v1.8.8": "1_8_8",
    "v1.9.1": "1_9_1",
    "v1.10.4": "1_10_4",
    "v1.11.7": "1_11_7",
}
ARCHITECTURE = 'x86_64'
OS = os.getenv('PARITY_OS', 'debian')


@toolz.curry
def fill_default_request_params(version, os=OS, architecture=ARCHITECTURE):
    params = {'version': version, 'os': os, 'architecture': architecture}
    return params


@toolz.functoolz.memoize
def get_parity_release_json(**kwargs):
    try:
        return requests.get(
            URI_QUERY_URL,
            params=kwargs).json()
    except JSONDecodeError as json_err:
        raise EnvironmentError("Could not find parity release for %s with %r" % (
            URI_QUERY_URL,
            kwargs,
        )) from json_err


@to_tuple
def get_binary_uri(releases_json):
    for release in releases_json:
        binary_uri = ((uri.get('downloadUrl', None), uri.get('checksum', None))
                      for uri in release.get('files', tuple())
                      if uri.get('name') == 'parity')
        yield next(binary_uri)


def get_executable_path(version_string):
    identifier = VERSION_STRINGS[version_string]
    base_path = os.environ.get('PARITY_BASE_INSTALL_PATH', BASE_BIN_PATH)
    path = os.path.join(base_path, 'parity-{0}'.format(identifier))
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
        try:
            download_binary(path, uri, checksum)
        except AssertionError as exc:
            raise Exception("failed to download binary at uri %r with params %r" % (
                uri,
                params,
            )) from exc

    return path


def download_binary(path, uri, checksum):
    r = get_binary_stream(uri)
    total_size = int(r.headers.get('content-length', 0))
    os.makedirs(os.path.dirname(path), exist_ok=True)
    digest = hashlib.sha256()
    with open(path, 'wb') as f:
        with tqdm(total=total_size,
                  unit='B',
                  unit_scale=True,
                  unit_divisor=1024) as pbar:
            for data in r.iter_content(32 * 1024):
                f.write(data)
                pbar.update(len(data))
                digest.update(data)
    hex_digest = digest.hexdigest()
    assert hex_digest == checksum, "digest vs checksum: %r vs %r" % (hex_digest, checksum)
    chmod_plus_x(path)


def chmod_plus_x(executable_path):
    current_st = os.stat(executable_path)
    os.chmod(executable_path, current_st.st_mode | stat.S_IEXEC)


def get_binary_stream(uri):
    resp = requests.get(uri, stream=True)
    if resp.status_code == 200:
        return resp
    else:
        resp.raise_for_status()


if __name__ == '__main__':
    install_parity(sys.argv[1])
