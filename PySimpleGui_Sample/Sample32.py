"""
入力

ユーザーからの入力を受け付けるためのポップアップウィンドウです。
テキスト入力フィールドやボタンを配置して情報の収集に使用します。
"""

import PySimpleGUI as sg

layout = [
    [sg.Text("Enter your name:"), sg.InputText(key="-NAME-")],
    [sg.Button("Submit")]
]

window = sg.Window("PopupGetText Widget Example", layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    if event == "Submit":
        user_name = values["-NAME-"]
        sg.popup(f"Hello, {user_name}!")

window.close()