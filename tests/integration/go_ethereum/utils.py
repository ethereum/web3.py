import asyncio
import signal
import socket
import time

import aiohttp
import requests


def wait_for_socket(ipc_path, timeout=30):
    start = time.time()
    while time.time() < start + timeout:
        try:
            sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
            sock.connect(ipc_path)
            sock.settimeout(timeout)
        except OSError:
            time.sleep(0.01)
        else:
            break


async def wait_for_async_socket(ipc_path, timeout=30):
    start = time.time()
    while time.time() < start + timeout:
        try:
            await asyncio.open_unix_connection(ipc_path)
        except OSError:
            time.sleep(0.01)
        else:
            break


def wait_for_http(endpoint_uri, timeout=60):
    start = time.time()
    while time.time() < start + timeout:
        try:
            requests.get(endpoint_uri)
        except requests.ConnectionError:
            time.sleep(0.01)
        else:
            break


async def wait_for_aiohttp(endpoint_uri, timeout=60):
    start = time.time()
    while time.time() < start + timeout:
        try:
            async with aiohttp.ClientSession() as session:
                await session.get(endpoint_uri)
        except aiohttp.client_exceptions.ClientConnectorError:
            time.sleep(0.01)
        else:
            break


def wait_for_popen(proc, timeout):
    start = time.time()
    while time.time() < start + timeout:
        if proc.poll() is None:
            time.sleep(0.01)
        else:
            break


def kill_proc_gracefully(proc):
    if proc.poll() is None:
        proc.send_signal(signal.SIGINT)
        wait_for_popen(proc, 13)

    if proc.poll() is None:
        proc.terminate()
        wait_for_popen(proc, 5)

    if proc.poll() is None:
        proc.kill()
        wait_for_popen(proc, 2)
