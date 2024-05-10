"""
Canvas

図形やグラフィックスを描画するための領域を提供するウィジェットです。
カスタムな描画を行いたい場合に使用します。
"""

import PySimpleGUI as sg

layout = [
    [sg.Canvas(size=(200, 100), background_color="white", key="-CANVAS-")],
    [sg.Button("Draw Circle")]
]
window = sg.Window("Canvas Widget Example", layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    if event == "Draw Circle":
        canvas = window["-CANVAS-"]
#        canvas.draw_circle((100, 50), 30, fill_color="red", line_color="black")

window.close()