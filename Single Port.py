import nmap
import re


class Singular:
    ip_addpattern = re.compile(
        "^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$|^(?:[0-9]{1,3}\.){3}[0-9]{1,3}\/[0-9]{1,4}$"
    )
    port_rangepattern = re.compile("([0-9]+)")

    min_port = 0
    max_port = 65535

    open_ports = []
    while True:
        ip_entered = input("\nEnter the IP address that you want scan: ")
        if ip_addpattern.search(ip_entered):
            print(f"{ip_entered} is a valid adress")
            break

    while True:
        a = input("Enter the port: ")
        alfa = int(a)
        if alfa:
            nMap = nmap.PortScanner()
            for port in range(alfa, alfa + 1):
                try:
                    result = nMap.scan(ip_entered, str(port))
                    port_status = result["scan"][ip_entered]["tcp"][port]["state"]
                    print(f"Port {port} is {port_status}")
                except:
                    print(f"Cannot scan port {port}.")
        cont = input("Do you want to continue scanning ports? ")
        if cont == "no":
            break
