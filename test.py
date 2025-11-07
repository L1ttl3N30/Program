from pynput import keyboard


log =""
def on_press(key):
    print(key)


listener = keyboard.Listener(on_press=on_press)
with listener:
    listener.join()
    log = log + str(key)
print(log)
