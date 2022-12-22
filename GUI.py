import sys
import PySimpleGUI as sg
import webbrowser
import os

class GUI:
    def __init__(self):
        sg.theme('DefaultNoMoreNagging')

        urls = {
                    'GitHub':'https://github.com/das-in',
                    'LinkedIn':'https://www.linkedin.com/company/das-in/',
                    'Facebook':'https://www.facebook.com/dasingolstadt',
                }

        self.layout = [
                [sg.Image(GUI.resource_path('Logo.png'))],
                [sg.Text('Location of PDF from KU Campus (with lecture timetable):')],
                [sg.Input(key = '-LocInput-'), sg.FileBrowse(file_types=(('pdf', '*.pdf'),))],
                [sg.Text('Location of ICAL file to be saved:')],
                [sg.Input(key = '-LocICAL-'), sg.FileSaveAs(file_types=(('ical', '*.ical'),))], 
                [sg.Text('Additional Options (data to be included for each appointment):')],
                [sg.Checkbox('all', default = True, key = '-RadioAll-'), sg.Text('or name + time +'), sg.Checkbox('name of lecturer', key = '-RadioLectureName-'), sg.Checkbox('room', key = '-RadioRoom-')],
                [sg.Button('OK'), sg.Button('Cancel')]
            ]

        self.layout2 = [
                [sg.Image(GUI.resource_path('Logo.png'))],
                [sg.Text('Thank you for using PDF-to-ICAL-Converter.')],
                [sg.Text('Your ICAL file is saved to:')],
                [sg.Input(key = '-LocICAL-', disabled = True)],
                [sg.Text('D.A.S. IN thanks the contributors of this project:')],
                [sg.Text('- Michael Betzke')],
                [sg.Text('- Vincent Bläske')],
                [sg.Text('- André Konersmann')],
                [sg.Text('- Florian Korn')],
                [sg.Text('- Paul Posselt')],
                [sg.Text('Any wishes, bugs or you want to join D.A.S. IN?')],
                [sg.Text('- Email: das.ingolstadt@gmail.com')],
                [sg.Text('- https://github.com/das-in', text_color = 'blue', tooltip = urls['GitHub'], enable_events = True, key = urls['GitHub'])],
                [sg.Text('- https://www.linkedin.com/company/das-in/', text_color = 'blue', tooltip = urls['LinkedIn'], enable_events = True, key = urls['LinkedIn'])],
                [sg.Text('- https://www.facebook.com/dasingolstadt', text_color = 'blue', tooltip = urls['Facebook'], enable_events = True, key = urls['Facebook'])], 
                [sg.Button('OK'), sg.Button('Cancel')]
            ]
        
        self.window = GUI.windowBuild(self.layout, False)
        self.window2 = GUI.windowBuild(self.layout2, True)
        self.values = GUI.executeGUI(self.window, self.window2)

    def executeGUI(window, window2):
        while True:
            event, values = window.read()
            # End program if user cloeses window or presses OK
            if event == 'OK' or event == sg.WIN_CLOSED or event == 'Cancel':
                window2['-LocICAL-'].update(str(values['-LocICAL-']))
                window.close()
                while True:
                    event2, values2 = window2.read()
                    if event2.startswith('https://'):
                        webbrowser.open(event2)
                    if event2 == 'OK' or event2 == sg.WIN_CLOSED or event2 == 'Cancel':
                        break
                break

        window2.close()

        return values

    def windowBuild(layout, finalize: bool):
        sg.theme('DefaultNoMoreNagging')
        return sg.Window('PDF to ICAL Converter', layout, finalize = finalize)

    def resource_path(relative_path):
        try:
            base_path = sys._MEIPASS
        except Exception:
            base_path = os.path.abspath(".")

        return os.path.join(base_path, relative_path)

        
        