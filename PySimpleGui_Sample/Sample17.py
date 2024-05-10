"""
Radio

ラジオボタンを表示し、複数の選択肢から1つを選ぶためのウィジェットです。
"""

import PySimpleGUI as sg

layout = [
    [sg.Radio("Option 1", "radio_group", default=True), sg.Radio("Option 2", "radio_group")],
    [sg.Button("Submit")]
]
window = sg.Window("Radio Widget Example", layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    if event == "Submit":
        option = "Option 1" if values[0] else "Option 2"
        sg.popup(f"Selected option: {option}")

window.close()