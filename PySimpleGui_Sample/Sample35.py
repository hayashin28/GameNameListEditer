"""
ウィンドウのサイズと位置について

ウィンドウのサイズや位置を指定する方法について説明します。
ウィンドウの初期表示位置やサイズを設定できます。
"""

import PySimpleGUI as sg

layout = [
    [sg.Text("Window Size and Position Example")],
    [sg.Button("Exit")]
]

window = sg.Window("Window Size and Position Example", layout, size=(300, 200), location=(100, 100))

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break

window.close()