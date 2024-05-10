"""
Listbox

リストから選択肢を選ぶためのウィジェットです。
複数の項目から1つ以上を選択できます。
"""

import PySimpleGUI as sg

choices = ["Option 1", "Option 2", "Option 3"]
layout = [
    [sg.Listbox(choices, size=(20, 3))],
    [sg.Button("Submit")]
]
window = sg.Window("Listbox Widget Example", layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    if event == "Submit":
        selected_options = values[0]
        sg.popup(f"Selected options: {', '.join(selected_options)}")

window.close()