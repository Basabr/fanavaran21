import socket
import threading

def receive_messages(sock):
    while True:
        try:
            msg = sock.recv(1024).decode()
            if msg:
                print("\n" + msg)
        except:
            print("Connection lost.")
            break

def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_ip = input("Enter server IP address: ")
    client.connect((server_ip, 12345))

    name = input("Enter your name: ")
    thread = threading.Thread(target=receive_messages, args=(client,))
    thread.start()

    while True:
        msg = input()
        if msg.lower() == "exit":
            break
        full_msg = f"{name}: {msg}"
        client.send(full_msg.encode())

    client.close()

main()
