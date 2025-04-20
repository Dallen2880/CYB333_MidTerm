import socket

# Create a TCP/IP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = '127.0.0.1'  # Must match server host
port = 65432        # Must match server port

try:
    # Connect to server
    client_socket.connect((host, port))
    print(f"[+] Connected to server at {host}:{port}")

    # Send a message
    client_socket.send("Hello from the client!".encode())

    # Receive response
    response = client_socket.recv(1024).decode()
    print(f"[Server]: {response}")

except ConnectionRefusedError:
    print("[!] Could not connect. Server may not be running.")
except Exception as e:
    print(f"[!] Error: {e}")

finally:
    client_socket.close()
    print("[+] Client shutdown")
