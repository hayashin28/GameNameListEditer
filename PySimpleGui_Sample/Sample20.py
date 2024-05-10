"""
Slider

数値の範囲を選択するためのウィジェットです。
最小値と最大値、初期値を指定できます。
"""

import PySimpleGUI as sg

layout = [
    [sg.Slider(range=(0, 100), default_value=50, orientation="h", size=(20, 15))],
    [sg.Button("Submit")]
]
window = sg.Window("Slider Widget Example", layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    if event == "Submit":
        selected_value = values[0]
        sg.popup(f"Selected value: {selected_value}")

window.close()