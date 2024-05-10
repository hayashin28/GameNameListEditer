"""
ウィンドウのクローズイベント

GUIプログラム内で最も一般的な終了条件は、ウィンドウがクローズされたときです。
ウィンドウがクローズされると、プログラムはイベントループから抜けて終了します。
以下のコードは、ウィンドウのクローズイベントを処理する例です。
"""

import PySimpleGUI as sg

layout = [[sg.Text("Hello, PySimpleGUI!")], [sg.Button("OK")]]
window = sg.Window("Exit Example", layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break  # ウィンドウが閉じられたらプログラムを終了

window.close()