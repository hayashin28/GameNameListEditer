"""
ウィジェットへの名前の付与

ウィジェットに名前を付与することで、特定のウィジェットを識別しやすくなります。
以下のコードは、名前付きのボタンを配置する例です。
"""

import PySimpleGUI as sg

layout = [[sg.Text("Hello, PySimpleGUI!")], [sg.Button("OK", key="ok_button")]]
window = sg.Window("Named Widget Example", layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    if event == "ok_button":
        sg.popup("OK button clicked!")

window.close()