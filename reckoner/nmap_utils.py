import subprocess
import nmap

def os_nmap_host_enum(ip_addr):
    print(f"[*] Enumerating {ip_addr}")
    try:
        results = subprocess.check_output(['nmap', '-sV', '-sV', ip_addr])
    except subprocess.CalledProcessError:
        return
    else:
        results = [line for line in results.decode().split('\n')]
        for line in results:
            print(line)

