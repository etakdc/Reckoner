import re
import nmap_utils

def port_scan(grepable_file):

    with open(grepable_file, 'r') as file_handler:
        hosts_ips = []
        for line in file_handler:
            if 'Host:' in line:
                ip = re.search(r'(?<=Host:\s).*(?=\s\()', line).group()
                hosts_ips.append(ip)

    for ip_addr in hosts_ips:
        nmap_utils.os_nmap_host_enum(ip_addr)

