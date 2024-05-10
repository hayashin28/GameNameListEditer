"""
Spin

数値の選択や調整を行うためのウィジェットです。
最小値と最大値を指定できます。
"""

import PySimpleGUI as sg

layout = [
    [sg.Spin(values=list(range(1, 11)), initial_value=5, size=(5, 1))],
    [sg.Button("Submit")]
]
window = sg.Window("Spin Widget Example", layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    if event == "Submit":
        selected_value = values[0]
        sg.popup(f"Selected value: {selected_value}")

window.close()