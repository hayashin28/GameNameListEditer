"""
リサイズ可能にする設定

ウィンドウのリサイズを許可するかどうかを設定するウィジェットです。
リサイズが許可されていれば、ユーザーはウィンドウのサイズを変更できます。
"""

import PySimpleGUI as sg

layout = [
    [sg.Text("Resizable Window Example")],
    [sg.Button("Exit")]
]

window = sg.Window("Resizable Window Example", layout, resizable=True)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break

window.close()