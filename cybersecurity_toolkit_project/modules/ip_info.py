import socket

def get_ip_info(target):
    try:
        ip = socket.gethostbyname(target)
        print("IP Address:", ip)
        host = socket.gethostbyaddr(ip)
        print("Hostname:", host[0])
    except socket.error:
        print("Unable to retrieve information")