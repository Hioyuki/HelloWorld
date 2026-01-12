import socket
import datetime

# Configuration
IP = "127.0.0.1"
PORT = 9999

# 1. Create a TCP socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Risk mitigation: allow instant port reuse
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) 

# 2. Bind and Listen
server.bind((IP, PORT))
server.listen(1)
print(f"[*] Server listening on {IP}:{PORT}")

# 3. Accept connection
client_socket, addr = server.accept()
print(f"[*] Accepted connection from {addr}")

try:
    while True:
        # Receive request from client
        data = client_socket.recv(1024).decode('utf-8')
        if not data or data.lower() == "exit":
            break
        
        print(f"[*] Client requested: {data}")
        
        # Additional Requirement: 3 different response types
        if "time" in data.lower():
            response = f"Server Time: {datetime.datetime.now().strftime('%H:%M:%S')}"
        elif "hello" in data.lower():
            response = "Hello from the server! Connection established."
        elif "status" in data.lower():
            response = "Server is running smoothly on Python 3."
        else:
            response = f"ACK: Received '{data}'"
            
        # Send response back to client
        client_socket.send(response.encode('utf-8'))
finally:
    client_socket.close()
    server.close()
    print("[*] Server connection closed.")
