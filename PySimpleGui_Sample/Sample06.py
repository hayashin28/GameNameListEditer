"""
ウィジェットのサイズ設定

ウィジェットのサイズを設定するには、ウィジェットのインスタンス生成時にsize引数を指定します。
例えば、以下のコードは、テキストを表示するウィンドウを作成し、テキストの幅と高さを設定しています。
"""

import PySimpleGUI as sg

layout = [[sg.Text("Hello, PySimpleGUI!", size=(20, 2))], [sg.Button("OK")]]
window = sg.Window("Size Example", layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == "OK":
        break

window.close()