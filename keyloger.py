import keyboard

print("Press 0 to stop")

with open("recorded.txt", "a") as file:

    def key_pressed(key):
        if key.name == 'space':
            file.write(' ')
        elif key.name == '@':
            file.write('@')
        elif key.name == 'enter':
            file.write('\n')
        else:
            file.write(key.name)

    keyboard.on_press(key_pressed)
    keyboard.wait('0')

print("Recording finished")
