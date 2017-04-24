import socket

def main():
    s = "Hello, server"
    soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    soc.connect(("127.0.0.1", 5555))
    soc.send(s.encode())

    answer = soc.recv(1024).decode()
    print(answer)
    soc.close()


main()
