import nmap
import re
import logging

logging.basicConfig(
    filename="log.txt", encoding="utf-8", level=logging.DEBUG, format="%(message)s"
)

ros = input("Do you want to scan a single port or a range of ports? ")
if ros == "range":
    ip_addpattern = re.compile(
        "^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$|^(?:[0-9]{1,3}\.){3}[0-9]{1,3}\/[0-9]{1,4}$"
    )
    port_rangepattern = re.compile("([0-9]+)-([0-9]+)")

    port_min = 0
    port_max = 65535

    open_ports = []
    while True:
        ip_entered = input("\nEnter the IP address that you want scan: ")
        logging.info(f"IP Adress: {ip_entered}")
        if ip_addpattern.search(ip_entered):
            print(f"{ip_entered} is a valid adress")
            break

    while True:
        print("Please enter the range of ports you want to scan: ")
        port_range = input("Enter port range: ")
        logging.info(f"Port Range: {port_range}")
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
            logging.info(f"Port {port} is {port_status}")
        except:
            print(f"Cannot scan port {port}.")
            logging.info(f"Cannot scan port {port}.")
    logging.info("\n")
elif ros == "single":
    ip_addpattern = re.compile(
        "^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$|^(?:[0-9]{1,3}\.){3}[0-9]{1,3}\/[0-9]{1,4}$"
    )
    port_rangepattern = re.compile("([0-9]+)")

    min_port = 0
    max_port = 65535

    open_ports = []
    while True:
        ip_entered = input("\nEnter the IP address that you want scan: ")
        logging.info(f"IP Adress: {ip_entered}")
        if ip_addpattern.search(ip_entered):
            print(f"{ip_entered} is a valid adress")
            break

    while True:
        a = input("Enter the port: ")
        alfa = int(a)
        logging.info(f"Port Number: {a}")
        if alfa:
            nMap = nmap.PortScanner()
            for port in range(alfa, alfa + 1):
                try:
                    result = nMap.scan(ip_entered, str(port))
                    port_status = result["scan"][ip_entered]["tcp"][port]["state"]
                    print(f"Port {port} is {port_status}")
                    logging.info(f"Port {port} is {port_status}")
                except:
                    print(f"Cannot scan port {port}.")
                    logging.info(f"Cannot scan port {port}.")
        cont = input("Do you want to continue scanning ports? ")
        if cont == "no":
            logging.info("\n")
            break
