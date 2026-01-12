import socket

IP = "127.0.0.1"
PORT = 9999

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((IP, PORT))

print("[*] サーバーに接続しました。'exit' と打つと終了します。")

while True:
    # キーボードから入力を受け取る
    msg = input("メッセージを入力してください >> ")
    
    client.send(msg.encode('utf-8'))
    
    if msg.lower() == "exit":
        break
        
    # サーバーからの返信を表示
    response = client.recv(1024).decode('utf-8')
    print(f"[Server]: {response}")

client.close()