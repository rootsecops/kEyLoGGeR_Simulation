

import socket

HOST = "127.0.0.1" 
PORT = 4444         

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(1)

print(f"[+] Attacker server listening on {HOST}:{PORT} ...")
conn, addr = server.accept()
print(f"[+] Connection from {addr}")

try:
    while True:
        data = conn.recv(1024)
        if not data:
            break
        print(data.decode("utf-8"), end="", flush=True)
except KeyboardInterrupt:
    print("\n[!] Server stopped by user")
finally:
    conn.close()
    server.close()
