#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import sys
import requests
import datetime as dt

from ping21 import is_compatible, get_server_info

__all__ = ["get21"]


def get21(uri, wait_timeout=5, headers=None):
    """ runs HTTP GET against the url.

    Args:
        url (str): A url to run GET against.
        wait_timeout (int): Optional timeout in seconds for request (default is 5)
        headers (dict): Optional headers to send with the request

    Raises:
        ValueError: if the url is malformed or GET cannot be performed on it.
    Returns:
        dict: A dictionary containing GET information.

    """
    # Default the headers
    if headers is None:
        headers = {}

    if not is_compatible():
        return

    start = dt.datetime.now()
    ret = requests.get(uri, timeout=wait_timeout, headers=headers)
    finish = dt.datetime.now()

    # Get elapsed time in milliseconds
    elapsed = int((finish - start).total_seconds() * 1000)

    res = {'status_code' : ret.status_code, 'reason' : ret.reason, 'elapsed_ms': elapsed}

    info = {
        'get': res,
        'server': get_server_info(),
    }
    return info

if __name__ == '__main__':
    url = sys.argv[1]
    data = get21(url)
    formatted_data = json.dumps(data, indent=4, sort_keys=True)
    print(formatted_data)
