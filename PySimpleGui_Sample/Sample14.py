"""
Multiline

複数行のテキスト入力を受け付けるためのウィジェットです。
複数行のテキストを編集する場合に使用します。
"""

import PySimpleGUI as sg

layout = [
    [sg.Multiline("Enter your notes here:", size=(30, 5))],
    [sg.Button("Save")]
]
window = sg.Window("Multiline Widget Example", layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    if event == "Save":
        notes = values[0]
        sg.popup(f"Notes saved:\n{notes}")

window.close()