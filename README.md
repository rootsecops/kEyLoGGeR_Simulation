# 🔑 Keylogger Simulation (Educational Project)

This project demonstrates a **simulated keylogger system** built in Python for **educational and research purposes only**.  
It showcases how keystrokes can be captured locally and sent to a remote server, helping students and researchers understand **keylogging mechanisms** and **data exfiltration concepts** in a controlled, safe environment.  

---

## ✨ Features
- **Keylogger Client** – Captures keyboard input and forwards it to a server.  
- **Attacker Server** – Receives, logs, and stores keystroke data from connected clients.  
- **Demo Script** – Quick demonstration of client-server communication in action.  
- **Build Artifacts** – Includes packaging files for creating an executable version of the client.  

---

## 📂 Project Structure
```

.
├── keylogger\_client.py      # Main client script (captures & sends keystrokes)
├── attacker\_server.py       # Server script (receives & stores keystrokes)
├── demo.py                  # Demonstration script
├── keylogger\_client.spec    # PyInstaller build spec for client
├── build/                   # Build artifacts / packaged files
└── requirements.txt         # Python dependencies

````

---

## 🚀 Usage

### 1. Start the Server
Run the attacker server to listen for incoming connections:
```bash
python attacker_server.py
````

### 2. Launch the Client

Start the keylogger client:

```bash
python keylogger_client.py
```

### 3. Run the Demo

To quickly see the client ↔ server interaction:

```bash
python demo.py
```

---

## ⚙️ How It Works (Technical Overview)

1. **Client (Victim Machine)**

   * Runs `keylogger_client.py`.
   * Uses a Python library (e.g., `pynput`) to monitor keyboard events.
   * Every keystroke is captured in real time.
   * The captured data is sent over a TCP socket connection to the attacker server.

2. **Server (Attacker Machine)**

   * Runs `attacker_server.py`.
   * Listens on a chosen port for incoming client connections.
   * Receives keystroke data from clients and writes it to a log file (or displays it live).

3. **Data Flow**

   ```
   [Keyboard Input] → [Keylogger Client] → [TCP Socket] → [Attacker Server] → [Log File]
   ```

4. **Demo Script (`demo.py`)**

   * Automates running both the server and client.
   * Provides a quick simulation of keystrokes being captured and transmitted.

This setup is **intentionally simple** so that students can clearly see how each component works without extra complexity.

---

## 🖼 Architecture Diagram

```plaintext
     ┌────────────────┐
     │  User Keyboard │
     └───────┬────────┘
             │ (1. Capture Keystrokes)
             ▼
     ┌────────────────────┐
     │ Keylogger Client   │
     │ (keylogger_client) │
     └───────┬────────────┘
             │ (2. Send via TCP)
             ▼
     ┌────────────────────┐
     │ Attacker Server    │
     │ (attacker_server)  │
     └───────┬────────────┘
             │ (3. Store Logs)
             ▼
     ┌────────────────┐
     │   Log File     │
     └────────────────┘
```

---

## 🛠 Installation

1. Install **Python 3.x**.
2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

---

## 📌 Requirements

* Python **3.x**
* Dependencies listed in `requirements.txt`

---

## ⚠️ Disclaimer

This project is intended **strictly for educational and research purposes**.
Do **not** use it for malicious activities. Running keylogger software without explicit authorization is **illegal and unethical**.
Use it only in controlled environments (such as labs, test machines, or coursework).
