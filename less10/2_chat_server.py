import socket, threading

class Client_handler(threading.Thread):
    def __init__(self, soc, clients):
        threading.Thread.__init__(self)
        self.soc = soc
        self.clients = clients

    def run(self):
        while True:
            message = self.soc.recv(1024).decode()
            message_array = message.split(':')
            if message_array[0] == 'name':
                self.clients[message_array[1]] = self.soc
            elif message_array[0] == 'list':
                output = ""
                for key in self.clients.keys():
                    output += key + '\n'
                self.soc.send(output.encode())
            elif message_array[0] == 'broadcast':
                sender = ""
                for key, value in self.clients.items():
                    if value == self.soc:
                        sender = key
                        break
                output = sender + ":" + message_array[1]
                for value in self.clients.values():
                    value.send(output.encode())
            else:
                sender = ""
                for key, value in self.clients.items():
                    if value == self.soc:
                        sender = key
                        break
                output = sender + ":" + message_array[1]
                rec_socket = self.clients[message_array[0]]
                rec_socket.send(output.encode())




def main():
    soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    soc.bind(("0.0.0.0", 3391))
    soc.listen(5)
    clients = {}
    while True:
        client_socket, addr = soc.accept()
        handler = Client_handler(client_socket, clients)
        handler.start()


main()