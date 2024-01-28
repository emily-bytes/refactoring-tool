# # Start your program and a GUI is generated
# # https://www.pysimplegui.org/en/latest/

import PySimpleGUI as sg

sg.theme('BluePurple')   # Add a touch of color
# All the stuff inside your window.
layout = [  [sg.Text('This tool analyzes the code in your file and detects duplicated code. ')],
            [sg.Button('Upload File'), sg.Button('Start Analysis'), sg.Button('Exit')] ]

# Create the Window
window = sg.Window('Code Smell Detector and Refactoring Tool', layout)

# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == 'Upload File':
        layout = [[sg.T("")], [sg.Text("Choose a file: "), sg.Input(), sg.FileBrowse(key="-IN-")],[sg.Button("Submit")]]

        #Building Window
        window = sg.Window('My File Browser', layout, size=(600,150))
    
        while True:
            event, values = window.read()
            if event == sg.WIN_CLOSED or event=="Exit":
                break
            elif event == "Submit":
                print(values["-IN-"])

    if event == sg.WIN_CLOSED or event == 'Exit': # if user closes window or clicks Exit
        break
    print('You entered ', values[0])

window.close()
          