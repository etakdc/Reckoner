# -*- coding: utf-8 -*-
"""
    Port Scanner
    ~~~~~~~~~~~~~~~~

    Various port scanner implementations

    * Subprocess

    :copyright: © 2018 by the etakdc.
    :license: BSD, see LICENSE for more details.
"""
import socket
import sys


def scan_port(host, port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = s.connect_ex((host, port))
        if result == 0:
            print(f"Port #{port} is open")
            s.close()
            return port
        else:
            s.close()
            return 'a'

    except KeyboardInterrupt:
        sys.exit(1)

