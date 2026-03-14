import socket
import threading

open_ports = []

def scan_port(target, port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.5)
        result = s.connect_ex((target, port))
        if result == 0:
            open_ports.append(port)
        s.close()
    except:
        pass

def port_scan(target):
    print("\nScanning ports...\n")
    threads = []
    for port in range(1, 1025):
        thread = threading.Thread(target=scan_port, args=(target, port))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    for port in open_ports:
        print(f"Port {port} OPEN")