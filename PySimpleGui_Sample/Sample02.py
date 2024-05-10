import PySimpleGUI as sg

layout = [[sg.Text('テキスト表示域', key='TEXT')],
          [sg.Input(key='INPUT'), sg.Button('ボタン', key='BUTTON')]]

window = sg.Window('タイトルバーに表示されるテキスト', layout)

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break
    if event == 'BUTTON':
        window['TEXT'].update(values['INPUT'])
window.close()
