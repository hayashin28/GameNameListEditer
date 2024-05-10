"""
Pane, Column

ウィジェットの配置を調整するためのウィジェットです。
横に並べたり、縦に積み重ねたりする際に使用します。
"""

import PySimpleGUI as sg

layout = [
    [sg.Pane([[sg.Text("Pane 1")]], size=(200, 100))],
    [sg.Column([[sg.Text("Column 1")]], size=(200, 100))],
    [sg.Button("Submit")]
]
window = sg.Window("Pane and Column Widget Example", layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    if event == "Submit":
        sg.popup("Submit button clicked!")

window.close()