"""
Checkbox

チェックボックスを表示し、オン・オフの状態を扱うためのウィジェットです。
"""

import PySimpleGUI as sg

layout = [
    [sg.Checkbox("Enable feature A"), sg.Checkbox("Enable feature B")],
    [sg.Button("Submit")]
]
window = sg.Window("Checkbox Widget Example", layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    if event == "Submit":
        feature_a = values[0]
        feature_b = values[1]
        sg.popup(f"Feature A: {feature_a}\nFeature B: {feature_b}")

window.close()