"""
Tree

階層構造を持つデータを表示するためのウィジェットです。
フォルダやファイルのツリー表示に適しています。
"""

import PySimpleGUI as sg

data = {
    "Folder 1": ["File 1-1", "File 1-2"],
    "Folder 2": ["File 2-1", "File 2-2"]
}
layout = [
    [sg.Tree(data, headings=["Folders", "Files"], auto_size_columns=True,
             num_rows=10, col_widths=[30, 20])],
    [sg.Button("Submit")]
]
window = sg.Window("Tree Widget Example", layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    if event == "Submit":
        sg.popup("Submit button clicked!")

window.close()