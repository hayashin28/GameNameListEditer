"""
Tab, TabGroup

複数のタブでコンテンツを切り替えるためのウィジェットです。
異なる情報や機能をタブごとにまとめて表示するのに便利です。
"""

import PySimpleGUI as sg

tab1_layout = [
    [sg.Text("Content of Tab 1")]
]
tab2_layout = [
    [sg.Text("Content of Tab 2")]
]
layout = [
    [sg.TabGroup([
        [sg.Tab("Tab 1", tab1_layout)],
        [sg.Tab("Tab 2", tab2_layout)]
    ])],
    [sg.Button("Submit")]
]
window = sg.Window("Tab Widget Example", layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    if event == "Submit":
        sg.popup("Submit button clicked!")

window.close()