"""
デザインテーマの設定

PySimpleGUIでは、ウィンドウのデザインテーマをカスタマイズすることができます。
以下のコードは、デザインテーマを設定したウィンドウを作成する例です。
"""

import PySimpleGUI as sg

sg.theme("DarkBlue3")  # デザインテーマを設定

layout = [[sg.Text("Hello, PySimpleGUI!")], [sg.Button("OK")]]
window = sg.Window("Theme Example", layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == "OK":
        break

window.close()