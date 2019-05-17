import re
import sys


class IpAddress:

    def __init__(self, ip_addr):
        self.address = IpAddress.validate_ip(ip_addr)

    @staticmethod
    def validate_ip(address):
        if re.search(r'^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$', address):
            return address
        else:
            return None
