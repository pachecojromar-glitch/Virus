# Simple Keylogger Project

## Description
This is a simple keylogger program made in Python for educational purposes.  
The program records the keys pressed on the keyboard and saves them into a text file.

This project is only for learning and testing on your own computer.


## How It Works

- The program listens to keyboard events.
- Every time a key is pressed, it writes the key into a file called `recorded.txt`.
- When you press `0`, the program stops recording.
- After stopping, it shows the message: "Recording finished".

## Requirements

- Python 3
- keyboard library

To install the required library, run:

py -m pip install keyboard

## How to Run

1. Open PowerShell or CMD in the project folder.
2. Run the following command:

py keyloger.py

⚠ On Windows, run the terminal as Administrator.

## Output

All pressed keys will be saved in:

recorded.txt

The file will be created automatically in the same folder.

## Example

If you type:

hello 123

The file will contain:

hello 123

## Author

Omar Pacheco
