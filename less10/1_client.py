import socket, threading
import select

class Read_soc(threading.Thread):
    def __init__(self,soc):
        threading.Thread.__init__(self)
        self.soc = soc

    def run(self):
        while True:
            mess = self.soc.recv(1024).decode()
            print(mess)


def main():
    soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    soc.connect(('127.0.0.1', 3391))
    select.select([soc],[soc],[])

    read_thread = Read_soc(soc)
    read_thread.start()

    while True:
        message = input()
        soc.send(message.encode())


main()