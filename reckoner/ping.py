# -*- coding: utf-8 -*-
"""
    ping
    ~~~~~~~~~~~~~~~~

    Various ping implementations:

    * Subprocess

    :copyright: © 2018 by the etakdc.
    :license: BSD, see LICENSE for more details.
"""
import subprocess


def subprocess_ping(ip_addr):
    """
    Use the subprocess module to call Unix built-in ping utility
    :param ip_addr: an ip address
    :return: ip string if reachable, None if not
    """
    try:
        subprocess.check_output(['ping', '-c', '1', ip_addr])
    except subprocess.CalledProcessError:
        return
    else:
        print(ip_addr)
        return ip_addr
