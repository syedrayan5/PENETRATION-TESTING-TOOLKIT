import socket

class PortScanner:
    def __init__(self, target):
        self.target = target

    def scan(self, start_port, end_port):
        open_ports = []
        for port in range(start_port, end_port + 1):
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
                sock.settimeout(1)
                result = sock.connect_ex((self.target, port))
                if result == 0:
                    open_ports.append(port)
        return open_ports