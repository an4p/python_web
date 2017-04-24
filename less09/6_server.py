import socket
import threading
class Client_Handler(threading.Thread):
    def __init__(self, soc):
        threading.Thread.__init__(self)
        self.soc = soc

    def run(self):
        message = self.soc.recv(1024).decode()
        message += "from server"
        self.soc.send(message.encode())
        self.soc.close()

def main():

    soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    soc.bind(("0.0.0.0", 5555))
    soc.listen(5)
    while True:
        client_socket, addr = soc.accept()

        handler = Client_Handler(client_socket)
        handler.start()






main()
