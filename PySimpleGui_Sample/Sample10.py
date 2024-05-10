"""
既存のウィジェットへのアクセス

ウィンドウ内の既存のウィジェットにアクセスするには、window[ウィジェットの名前]という形式でアクセスします。
以下のコードは、名前付きのテキストを更新する例です。
"""

import PySimpleGUI as sg

layout = [[sg.Text("Hello, PySimpleGUI!", key="output_text")], [sg.Button("Update")]]
window = sg.Window("Access Widget Example", layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    if event == "Update":
        window["output_text"].update()

window.close()