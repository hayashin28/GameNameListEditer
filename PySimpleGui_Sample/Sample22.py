"""
VerticalSeparator

垂直方向の区切り線を表示するためのウィジェットです。
ウィジェットのレイアウトを調整する際に使用します。
"""

import PySimpleGUI as sg

layout = [
    [sg.Text("Left side"), sg.VerticalSeparator(), sg.Text("Right side")],
    [sg.Button("Submit")]
]
window = sg.Window("VerticalSeparator Widget Example", layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    if event == "Submit":
        sg.popup("Submit button clicked!")

window.close()