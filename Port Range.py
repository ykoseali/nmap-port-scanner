import nmap
import re


class Range:
    ip_addpattern = re.compile(
        "^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$|^(?:[0-9]{1,3}\.){3}[0-9]{1,3}\/[0-9]{1,4}$"
    )
    port_rangepattern = re.compile("([0-9]+)-([0-9]+)")

    port_min = 0
    port_max = 65535

    open_ports = []
    while True:
        ip_entered = input("\nEnter the IP address that you want scan: ")
        if ip_addpattern.search(ip_entered):
            print(f"{ip_entered} is a valid adress")
            break

    while True:
        print("Please enter the range of ports you want to scan: ")
        port_range = input("Enter port range: ")
        valid_range = port_rangepattern.search(port_range.replace(" ", ""))
        if valid_range:
            port_min = int(valid_range.group(1))
            port_max = int(valid_range.group(2))
            break

    nMap = nmap.PortScanner()
    for port in range(port_min, port_max + 1):
        try:
            result = nMap.scan(ip_entered, str(port))
            port_status = result["scan"][ip_entered]["tcp"][port]["state"]
            print(f"Port {port} is {port_status}")
        except:
            print(f"Cannot scan port {port}.")
