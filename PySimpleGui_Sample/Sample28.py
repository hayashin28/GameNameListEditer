"""
OptionMenu

ドロップダウンメニューを表示するためのウィジェットです。
選択肢から1つを選ぶことができます。
"""

import PySimpleGUI as sg

choices = ["Option 1", "Option 2", "Option 3"]
layout = [
    [sg.OptionMenu(choices, default_value="Option 1")],
    [sg.Button("Submit")]
]
window = sg.Window("OptionMenu Widget Example", layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    if event == "Submit":
        selected_option = values[0]
        sg.popup(f"Selected option: {selected_option}")

window.close()