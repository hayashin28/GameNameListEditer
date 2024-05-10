"""
Text

テキストを表示するためのウィジェットです。
テキストウィジェットを使用することで、ユーザーに情報を表示することができます。
フォントや余白、枠線の設定も可能です。
"""

import PySimpleGUI as sg

layout = [[sg.Text("Hello, PySimpleGUI!")]]
window = sg.Window("Text Widget Example", layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break

window.close()