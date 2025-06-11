import socket

c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
c.connect(("localhost", 9999))
while True:
    # name = input("Enter your message: ")
    # c.send(bytes(name, "utf-8"))
    
    # print(c.recv(1024).decode("utf-8"))

    msg = input("Enter your message (type 'exit' to disconnect): ")
    c.send(msg.encode())
    
    if msg.lower() == "exit":
        print("Disconnected from server.")
        break

    # Receive response from server
    server_msg = c.recv(1024).decode()
    print(f"Server: {server_msg}")

    if server_msg.lower() == "exit":
        print("Server closed the connection.")
        break

c.close()
