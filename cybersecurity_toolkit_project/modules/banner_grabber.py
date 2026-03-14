import socket

def banner_grab(target, port):
    try:
        s = socket.socket()
        s.settimeout(2)
        s.connect((target, port))
        banner = s.recv(1024)
        print("Service Banner:", banner.decode(errors="ignore"))
        s.close()
    except:
        print("No banner detected")