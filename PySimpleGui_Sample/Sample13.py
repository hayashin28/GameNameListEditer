"""
InputText

ユーザーに文字を入力させるためのウィジェットです。
テキストボックスやパスワード入力フィールドとして使用できます。
イベントハンドリングや初期値の設定が可能です。
"""

import PySimpleGUI as sg

layout = [
    [sg.Text("Enter your name:"), sg.InputText()],
    [sg.Text("Enter your password:"), sg.InputText(password_char="*")],
    [sg.Button("Submit")]
]
window = sg.Window("InputText Widget Example", layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    if event == "Submit":
        name = values[0]
        password = values[1]
        sg.popup(f"Name: {name}\nPassword: {password}")

window.close()