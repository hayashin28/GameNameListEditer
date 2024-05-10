"""
ウィジェットのイベントハンドリングの有効化

PySimpleGUIでは、ウィジェットのイベント（ボタンクリックなど）を処理するために、
イベントハンドリングを有効化する必要があります。
以下のコードは、ボタンクリックイベントを処理する例です。
"""

import PySimpleGUI as sg

layout = [[sg.Text("Hello, PySimpleGUI!")], [sg.Button("OK")]]
window = sg.Window("Event Handling Example", layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    if event == "OK":
        sg.popup("Button clicked!")

window.close()