import contextlib
import json
import os
import pprint
import shutil
import sys
import time

from eth_utils import (
    to_text,
)

import common
import go_ethereum
from web3 import Web3
from web3.utils.toolz import (
    merge,
)

CHAIN_CONFIG = {
    "name": "CrossClient",
    "dataDir": "CrossClient",
    "engine": {
        "Ethash": {
            "params": {
                "minimumDifficulty": "0x020000",
                "difficultyBoundDivisor": "0x0800",
                "durationLimit": "0x0d",
                "blockReward": "0x4563918244F40000",
                "homesteadTransition": 0,
                "eip150Transition": 0,
                "eip160Transition": 10,
                "eip161abcTransition": 10,
                "eip161dTransition": 10
            }
        }
    },
    "params": {
        "gasLimitBoundDivisor": "0x0400",
        "registrar": "0x81a4b044831c4f12ba601adb9274516939e9b8a2",
        "eip155Transition": 10,
        "accountStartNonce": "0x0",
        "maximumExtraDataSize": "0x20",
        "minGasLimit": "0x1388",
        "networkID": "0x539",
        "eip98Transition": "0x7fffffffffffffff"
    },
    "genesis": {
        "seal": {
            "ethereum": {
                "nonce": "0x0000000000000042",
                "mixHash": "0x0000000000000000000000000000000000000000000000000000000000000000"
            }
        },
        "difficulty": "0x10000",
        "author": common.COINBASE,
        "timestamp": "0x00",
        "parentHash": "0x0000000000000000000000000000000000000000000000000000000000000000",
        "extraData": "0x3535353535353535353535353535353535353535353535353535353535353535",
        "gasLimit": "0x1000000"
    },
    "accounts": {
        common.COINBASE: {
            "balance": "1000000000000000000000000000",
            "nonce": "0",
            "builtin": {
                "name": "ecrecover", "pricing": {"linear": {"base": 3000, "word": 0}}
            }
        },
        common.UNLOCKABLE_ACCOUNT: {
            "balance": "1000000000000000000000000000",
            "nonce": "0",
            "builtin": {
                "name": "sha256", "pricing": {"linear": {"base": 60, "word": 12}}
            }
        },
        common.RAW_TXN_ACCOUNT: {
            "balance": "1000000000000000000000000000",
            "nonce": "0",
            "builtin": {
                "name": "ripemd160",
                "pricing": {"linear": {"base": 600, "word": 120}}
            }
        }
    }
}


def get_parity_binary():
    return 'parity'


@contextlib.contextmanager
def get_parity_process(
        parity_binary,
        datadir,
        ipc_path,
        keys_path,
        chain_config_file_path,
        parity_port):

    run_command = (
        parity_binary,
        '--base-path', datadir,
        '--ipc-path', ipc_path,
        '--no-ws',
        '--no-ui',
        '--no-warp',
        '--chain', chain_config_file_path,
        '--keys-path', keys_path,
        '--rpcapi', 'all',
        '--rpcport', parity_port,
        # '--author', common.COINBASE[2:],
    )
    print(' '.join(run_command))
    try:
        proc = common.get_process(run_command)
        yield proc
    finally:
        common.kill_proc_gracefully(proc)
        output, errors = proc.communicate()
        print(
            "Parity Process Exited:\n"
            "stdout:{0}\n\n"
            "stderr:{1}\n\n".format(
                to_text(output),
                to_text(errors),
            )
        )


@contextlib.contextmanager
def parity_export_blocks_process(
        parity_binary,
        datadir,
        chain_config_file_path,
        parity_port):

    run_command = (
        parity_binary,
        'export',
        'blocks', os.path.join(datadir, 'blocks_export.rlp'),
        '--base-path', datadir,
        '--no-ws',
        '--no-ui',
        '--no-warp',
        '--chain', chain_config_file_path,
        '--rpcapi', 'all',
        '--rpcport', parity_port,
        # '--author', common.COINBASE[2:],
    )
    print(' '.join(run_command))
    try:
        proc = common.get_process(run_command)
        yield proc
    finally:
        common.kill_proc_gracefully(proc)
        output, errors = proc.communicate()
        print(
            "Parity Process Exited:\n"
            "stdout:{0}\n\n"
            "stderr:{1}\n\n".format(
                to_text(output),
                to_text(errors),
            )
        )


def generate_parity_fixture(destination_dir):
    """
    The parity fixture generation strategy is to start a geth client with
    existing fixtures copied into a temp datadir.  Then a parity client
    is started is peered with the geth client.
    """
    with contextlib.ExitStack() as stack:

        geth_datadir = stack.enter_context(common.tempdir())

        geth_port = common.get_open_port()

        geth_ipc_path_dir = stack.enter_context(common.tempdir())
        geth_ipc_path = os.path.join(geth_ipc_path_dir, 'geth.ipc')

        geth_keystore_dir = os.path.join(geth_datadir, 'keystore')
        common.ensure_path_exists(geth_keystore_dir)
        geth_keyfile_path = os.path.join(geth_keystore_dir, common.KEYFILE_FILENAME)
        with open(geth_keyfile_path, 'w') as keyfile:
            keyfile.write(common.KEYFILE_DATA)

        genesis_file_path = os.path.join(geth_datadir, 'genesis.json')
        with open(genesis_file_path, 'w') as genesis_file:
            genesis_file.write(json.dumps(common.GENESIS_DATA))

        stack.enter_context(
            common.get_geth_process(
                common.get_geth_binary(),
                geth_datadir,
                genesis_file_path,
                geth_ipc_path,
                geth_port,
                str(CHAIN_CONFIG['params']['networkID']))
        )
        # set up fixtures
        common.wait_for_socket(geth_ipc_path)
        web3_geth = Web3(Web3.IPCProvider(geth_ipc_path))
        chain_data = go_ethereum.setup_chain_state(web3_geth)
        fixture_block_count = web3_geth.eth.blockNumber

        datadir = stack.enter_context(common.tempdir())

        keystore_dir = os.path.join(datadir, 'keys')
        os.makedirs(keystore_dir, exist_ok=True)
        parity_keyfile_path = os.path.join(keystore_dir, common.KEYFILE_FILENAME)
        with open(parity_keyfile_path, 'w') as keyfile:
            keyfile.write(common.KEYFILE_DATA)

        chain_config_file_path = os.path.join(datadir, 'chain_config.json')
        with open(chain_config_file_path, 'w') as chain_file:
            chain_file.write(json.dumps(CHAIN_CONFIG))

        parity_ipc_path_dir = stack.enter_context(common.tempdir())
        parity_ipc_path = os.path.join(parity_ipc_path_dir, 'jsonrpc.ipc')

        parity_port = common.get_open_port()
        parity_binary = get_parity_binary()

        parity_proc = stack.enter_context(get_parity_process(  # noqa: F841
            parity_binary=parity_binary,
            datadir=datadir,
            ipc_path=parity_ipc_path,
            keys_path=keystore_dir,
            chain_config_file_path=chain_config_file_path,
            parity_port=parity_port,
        ))

        common.wait_for_socket(parity_ipc_path)
        web3 = Web3(Web3.IPCProvider(parity_ipc_path))

        time.sleep(10)
        connect_nodes(web3, web3_geth)
        wait_for_chain_sync(web3, fixture_block_count)

        static_data = {
            'raw_txn_account': common.RAW_TXN_ACCOUNT,
            'keyfile_pw': common.KEYFILE_PW,
        }
        pprint.pprint(merge(chain_data, static_data))

        shutil.copytree(datadir, destination_dir)

        parity_proc = stack.enter_context(parity_export_blocks_process(  # noqa: F841
            parity_binary=parity_binary,
            datadir=destination_dir,
            chain_config_file_path=os.path.join(destination_dir, 'chain_config.json'),
            parity_port=parity_port,
        ))


def connect_nodes(w3_parity, w3_secondary):
    parity_peers = w3_parity.parity.netPeers()
    parity_enode = w3_parity.parity.enode()
    secondary_node_info = w3_secondary.admin.nodeInfo
    if secondary_node_info['id'] not in (node.get('id', tuple()) for node in parity_peers['peers']):
        w3_secondary.admin.addPeer(parity_enode)


def wait_for_chain_sync(web3, target):
    start_time = time.time()
    while time.time() < start_time + 120:
        current_block_number = web3.eth.blockNumber
        if current_block_number >= target:
            break
        else:
            time.sleep(0.1)
    else:
        raise ValueError("Not synced after wait period")


if __name__ == '__main__':
    fixture_dir = sys.argv[1]
    generate_parity_fixture(fixture_dir)
