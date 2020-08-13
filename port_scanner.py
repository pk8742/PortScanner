import threading
import socket
from queue import Queue

target = '192.168.43.1'
queue = Queue()
open_ports = []
def portscan(port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((target, port))
        return True
    except:
        return False

# print(portscan(80))
"""
for port in range(1, 1024):
    result = portscan(port)
    if result:
        print("Port {} is open".format(port))
    else:
        print("Port {} is close".format(port))
"""
def fill_queue(port_list):
    for port in port_list:
        queue.put(port)

def worker():
    while not queue.empty():
        port = queue.get()
        if(portscan(port)):
            print(f"Port {port} is open")
            open_ports.append(port)
#       else:
#           print(f"Port {port} is close")

port_list = range(1,1024)
fill_queue(port_list)

# threading
thread_list = []
for t in range(100):
    thread = threading.Thread(target=worker)
    thread_list.append(thread)
# to start threads
for thread in thread_list:
    thread.start()
    print(thread)

for thread in thread_list:
    thread.join()

print(f"open ports are: {open_ports}")

