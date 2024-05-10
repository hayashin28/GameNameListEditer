"""
Table

表形式のデータを表示するためのウィジェットです。
データの表示や編集に使用します。
"""

import PySimpleGUI as sg

data = [["John", 25, "Male"], ["Emily", 30, "Female"], ["Michael", 28, "Male"]]
layout = [
    [sg.Table(values=data, headings=["Name", "Age", "Gender"], display_row_numbers=False,
               auto_size_columns=False, justification="right")],
    [sg.Button("Submit")]
]
window = sg.Window("Table Widget Example", layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    if event == "Submit":
        sg.popup("Submit button clicked!")

window.close()