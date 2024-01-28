# Start your program and a GUI is generated

import PySimpleGUI as sg
import tkinter 

layout = [[sg.Text("This program allow you to upload a single file and detects/refactors code smells")], [sg.Button("OK")]]

# Create the window
window = sg.Window("Code Smell Detector and Refactoring Tool", layout)


# Users close the program through GUI 
# Create an event loop
while True:
    event, values = window.read()
    # End program if user closes window or
    # presses the OK button
    if event == "OK" or event == sg.WIN_CLOSED:
        break

window.close()

          