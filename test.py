import PySimpleGUI as sg

sg.theme('Default')

layout = [
          [sg.Image(r'C:\Eigene Dateien\DAS_IN\Projekte\Logo.png')],
          [sg.Text('Location of PDF from KU Campus (with lecture timetable):')],
          [sg.Input(), sg.FileBrowse()],
          [sg.Text('Location of ICAL file to be saved:')],
          [sg.Input(), sg.FileSaveAs()], 
          [sg.Text('Additional Options (data to be included for each appointment):')],
          [sg.Checkbox('all', default=True), sg.Checkbox('lecture name'), sg.Checkbox('room'), sg.Checkbox('lecturer name'), sg.Checkbox('others')],
          [sg.Button('OK'), sg.Button('Cancel')]
]

window = sg.Window('PDF to ICAL Converter', layout)

while True:
    event, values = window.read()
    # End program if user cloeses window or presses OK
    if event == 'OK' or event == sg.WIN_CLOSED or event == 'Cancel':
        break

window.close()