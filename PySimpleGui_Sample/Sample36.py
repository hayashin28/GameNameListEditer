"""
タイトルバーの有無

ウィンドウのタイトルバーを表示するかどうかを設定するウィジェットです。
タイトルバーなしでウィンドウを作成できます。
"""

import PySimpleGUI as sg

layout = [
    [sg.Text("No Title Bar Window Example")],
    [sg.Button("Exit")]
]

window = sg.Window("No Title Bar Window Example", layout, no_titlebar=True)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break

window.close()