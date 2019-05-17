# -*- coding: utf-8 -*-
"""
    Reckoner
    ~~~~~~~~~~~~~~~~


    :copyright: © 2018 by the etakdc.
    :license: BSD, see LICENSE for more details.
"""

import argparse
import sys
import time
import grepable_files
from multiprocessing import Pool
from IP import IpAddress
from ping import subprocess_ping
from port_scanner import scan_port
def main():

    """
        Option menu for the user. Only its executed if is this module is executed as main file.

        Available Options:
        --gcstar:
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('--pingsweep',
                        nargs=2,
                        metavar=(
                            'initial_addr', '/output/file'),
                        help='Perform a ping sweep and save to file reachable hosts'
                        )
    parser.add_argument('--portscan',
                        nargs=2,
                        metavar=(
                            'Remote_Host', 'port_range'),
                        help='Perform a port scan to given host'
                        )
    parser.add_argument('--grepable',
                        nargs=2,
                        metavar=(
                            'file', 'task'),
                        help='Perform tasks on grepable files'
                        )

    # Display help menu if zero arguments are given, in any other case enter the options menu

    if len(sys.argv) > 1:
        options = parser.parse_args()
        user_options(options)

    else:
        parser.print_help()
        sys.exit(0)


def user_options(options):
    """
    Handles the diverse user options given as argument in the script

    :param options: ArgumentParser Object
    :return:
    """
    if options.pingsweep is not None:
        initial_ip = options.pingsweep[0]
        out_file = options.pingsweep[1]
        if IpAddress.validate_ip(initial_ip) is not None:
            ping_sweep(initial_ip[:-2], out_file)
        else:
            print('[X] Invalid IP')
    elif options.portscan is not None:
        rhost = options.portscan[0]
        range = options.portscan[1]
        port_scan(rhost, range)
    elif options.grepable is not None:
        gfile = options.grepable[0]
        task = options.grepable[1]
        grepable_files_tasks(gfile, task)


def ping_sweep(ip, out_file):
    """
    Perform a ping sweep
    :param ip: ArgumentParser Object
    :param out_file: ArgumentParser Object
    :return:
    """
    start_time = time.time()
    ip_range = [f"{ip}.{i}" for i in range(255)]
    p = Pool(processes=len(ip_range))
    data = p.map(subprocess_ping, ip_range)
    p.close()

    # Write to file
    with open(out_file, 'w') as file_handler:
        for ip in data:
            if ip is not None:
                file_handler.write(f"{ip}\n")

    print("--- {} seconds ---".format(time.time() - start_time))
    print("--- {} mins ---".format((time.time() - start_time) / 60))


def port_scan(rhost, upper_limit):
    start_time = time.time()
    ports = [i for i in range(int(upper_limit))]
    product = [(rhost, port) for port in ports]
    with Pool() as pool:
        results = pool.starmap(scan_port, product)
    a = [i for i in results if i != 'a']
    print(a)




    print("--- {} seconds ---".format(time.time() - start_time))
    print("--- {} mins ---".format((time.time() - start_time) / 60))


def grepable_files_tasks(gfile, task):
    if task == 'enumeration':
        grepable_files.port_scan(gfile)


if __name__ == '__main__':
    main()