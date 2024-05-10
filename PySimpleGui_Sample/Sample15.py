"""
Button

ユーザーのアクションをトリガーするためのボタンです。
クリックされると特定のイベントが発生します。
"""

import PySimpleGUI as sg

layout = [[sg.Button("Click me")]]
window = sg.Window("Button Widget Example", layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    if event == "Click me":
        sg.popup("Button clicked!")

window.close()