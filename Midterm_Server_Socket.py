import socket

# Create a TCP/IP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to a local address and port
host = '127.0.0.1'  # localhost
port = 65432
server_socket.bind((host, port))

# Start listening for connections
server_socket.listen()
print(f"[+] Server listening on {host}:{port}")

try:
    # Accept a connection
    client_socket, addr = server_socket.accept()
    print(f"[+] Connected by {addr}")

    # Receive message from client
    message = client_socket.recv(1024).decode()
    print(f"[Client]: {message}")

    # Send response
    response = "Hello from the server!"
    client_socket.send(response.encode())

    # Close client connection
    client_socket.close()
    print("[+] Client disconnected")

except Exception as e:
    print(f"[!] Error: {e}")

finally:
    server_socket.close()
    print("[+] Server shutdown")
