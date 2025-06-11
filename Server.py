import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("socket created")

s.bind(("localhost", 9999)) #bind to ip and port

s.listen(3)
print("waiting for connection")

while True:
    c, addr = s.accept()
    # name = c.recv(1024).decode()

    print("connection from", addr)
    # # c.send(b"Thank you for connecting")
    # send = input("Enter your message: ")
    # c.send(send.encode())
    while True:
        client_msg = c.recv(1024).decode()
        if not client_msg or client_msg.lower() == "exit":
            print(f"Connection with {addr} closed.")
            break

        print(f"Client: {client_msg}")
        
        # Send response to client
        send_msg = input("Enter your message: ")
        c.send(send_msg.encode())
        
        if send_msg.lower() == "exit":
            print(f"Closing connection with {addr}")
            break

    c.close() 
    exit(0)