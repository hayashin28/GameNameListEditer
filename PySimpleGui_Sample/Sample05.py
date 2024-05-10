"""
特定のアクションによる終了

ユーザーが特定のアクション（ボタンクリックなど）を実行した場合にも、GUIプログラムを終了させることができます。
以下のコードは、ボタンクリックによってプログラムを終了する例です。
"""

import PySimpleGUI as sg

layout = [[sg.Text("Hello, PySimpleGUI!")], [sg.Button("Exit")]]
window = sg.Window("Exit Example", layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == "Exit":
        break  # ウィンドウが閉じられたか「Exit」ボタンがクリックされたらプログラムを終了

window.close()