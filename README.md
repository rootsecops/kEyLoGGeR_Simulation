# Keylogger Simulation

This project demonstrates a simulated keylogger system for educational and research purposes. It consists of a client that captures keystrokes and an attacker server that receives the logged data. The project is intended to showcase how keylogging and remote data exfiltration can be implemented in Python.

## Features
- **Keylogger Client**: Captures keyboard input and sends it to a remote server.
- **Attacker Server**: Receives and stores keystroke data from clients.
- **Demo Script**: Example usage and demonstration of the keylogger-client/server interaction.
- **Build Artifacts**: Contains files generated from packaging the client for distribution.

## File Structure
- `keylogger_client.py`: Main client script for capturing and sending keystrokes.
- `attacker_server.py`: Server script to receive and log keystrokes from clients.
- `demo.py`: Demonstration script for running the simulation.
- `keylogger_client.spec`: PyInstaller spec file for building the client executable.
- `build/`: Directory containing build artifacts and packaged files.

## Usage
### 1. Start the Attacker Server
Run the server to listen for incoming keystroke data:
```cmd
python attacker_server.py
```

### 2. Run the Keylogger Client
Start the client to begin capturing and sending keystrokes:
```cmd
python keylogger_client.py
```

### 3. Demo
Use `demo.py` to see a demonstration of the client-server interaction:
```cmd
python demo.py
```

## Installation

1. Install Python 3.x if not already installed.
2. Install required packages using pip:
	```cmd
	pip install -r requirements.txt
	```

## Requirements
- Python 3.x
- All required packages are listed in `requirements.txt`.

## Disclaimer
This project is for educational and research purposes only. Do not use it for malicious activities. Always obtain proper authorization before running keylogger software on any system.
