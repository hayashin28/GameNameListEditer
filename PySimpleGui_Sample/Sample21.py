"""
Frame

ウィジェットをグループ化するための枠を表示するためのウィジェットです。
関連するウィジェットをまとめて表示する場合に使用します。
"""

import PySimpleGUI as sg

layout = [
    [sg.Frame("Group 1", [[sg.Text("Widget 1")]])],
    [sg.Frame("Group 2", [[sg.Text("Widget 2")]])],
    [sg.Button("Submit")]
]
window = sg.Window("Frame Widget Example", layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    if event == "Submit":
        sg.popup("Submit button clicked!")

window.close()