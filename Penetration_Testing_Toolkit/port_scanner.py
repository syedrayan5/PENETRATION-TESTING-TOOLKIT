import socket

def port_scanner(ip, port_range):
    open_ports = []
    for port in range(port_range[0], port_range[1] + 1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = sock.connect_ex((ip, port))
        if result == 0:
            open_ports.append(port)
        sock.close()
    return open_ports

# Usage
ip = '192.168.1.1'
port_range = (1, 65535)
print(f"Open ports: {port_scanner(ip, port_range)}")
