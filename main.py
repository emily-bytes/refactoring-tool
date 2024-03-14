import PySimpleGUI as sg
from CodeSmellDetector import CodeSmellDetector

# sources: https://www.pysimplegui.com/ using persistent window
# https://www.reddit.com/r/learnpython/comments/mosgc5/updating_text_with_pysimplegui/

def read_file(file_path):
    with open(file_path, 'r') as file:
        return file.read()

def upload_file(values, window):
    source_code = read_file(values['-FILE_PATH-'])
    window['-SOURCE_CODE-'].update(value = source_code)

def analyze_file_for_code_smells(values, window):
    source_code = read_file(values['-FILE_PATH-'])
    
    detector = CodeSmellDetector(source_code)
    long_methods, long_parameter_list = detector.find_long_method(), detector.find_long_parameter_list()
    duplicated_code, code_with_removed_duplicates = detector.find_duplicated_code()
    window['-ANALYSIS_RESULT-'].update(value = '\n'.join(long_methods) + '\n'.join(long_parameter_list) + '\n'.join(duplicated_code))
    window['-REFACTORED_CODE-'].update(value = code_with_removed_duplicates)

def run_gui():
    sg.theme('BluePurple')
    layout = [
        [sg.Text('Choose a file:'), sg.InputText(key='-FILE_PATH-'), sg.FileBrowse()],
        [sg.Multiline(size=(80, 10), key='-SOURCE_CODE-')],
        [sg.Button('Upload File'), sg.Button('Analyze File'), sg.Button('Cancel')],
        [sg.Multiline(size=(80, 10), key='-ANALYSIS_RESULT-')],
        [sg.Multiline(size=(80, 10), key='-REFACTORED_CODE-')],
    ]
    window = sg.Window('Code Smell Detection and Refactoring Tool', layout)
    
    while True:
        event, values = window.read()
        if event == sg.WINDOW_CLOSED or event == 'Cancel': break
        if event == 'Upload File': upload_file(values, window)
        if event == 'Analyze File': analyze_file_for_code_smells(values, window)
    window.close()

if __name__ == '__main__':
    run_gui()
