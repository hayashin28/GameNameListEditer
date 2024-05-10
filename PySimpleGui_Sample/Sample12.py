"""
Image

画像を表示するためのウィジェットです。
画像ファイルのパスを指定して表示することができます。
サイズの調整や配置も行えます。
"""

import PySimpleGUI as sg

layout = [[sg.Image("image.png")]]
window = sg.Window("Image Widget Example", layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break

window.close()