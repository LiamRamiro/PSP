#Enter an IP address and a port range where the program will then attempt to
# find open ports on the given computer by connecting to each of them.
# On any successful connections mark the port as open. 

import socket

def port_scanner(ip_address, port_range):
    open_ports = []
    for port in range(port_range[0], port_range[1]+1):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)
        result = s.connect_ex((ip_address, port))
        if result == 0:
            open_ports.append(port)
        s.close()
    return open_ports

# Example usage
print(port_scanner('127.0.0.1', (1, 1024)))