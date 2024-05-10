"""
MenuBar

アプリケーションのメニューバーを表示するためのウィジェットです。
さまざまなコマンドやアクションをメニュー形式で提供できます。
"""

import PySimpleGUI as sg

menu_def = [
    ["File", ["Open", "Save", "Exit"]],
    ["Edit", ["Cut", "Copy", "Paste"]]
]
layout = [
    [sg.Menu(menu_def)],
    [sg.Button("Submit")]
]
window = sg.Window("MenuBar Widget Example", layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    if event == "Submit":
        sg.popup("Submit button clicked!")

window.close()