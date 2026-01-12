import socket

IP = "127.0.0.1"
PORT = 9999

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    client.connect((IP, PORT))
    print("[*] Server connected. Type 'exit' to quit.")

    while True:
        msg = input("Message >> ")
        client.send(msg.encode('utf-8'))
        
        if msg.lower() == "exit":
            break
            
        response = client.recv(1024).decode('utf-8')
        print(f"[Server]: {response}")

finally:
    client.close()