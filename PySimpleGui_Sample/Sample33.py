"""
報告，確認のためのポップアップ表示

ユーザーに対して重要な情報を表示したり、アクションを確認するために
ポップアップウィンドウを使用することがあります。
sg.popup関数を使用して簡単にポップアップを表示できます。
"""

import PySimpleGUI as sg

layout = [
    [sg.Text("Report and Confirmation Popup Example")],
    [sg.Button("Show Report"), sg.Button("Confirm Action")]
]

window = sg.Window("Report and Confirmation Popup Example", layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    if event == "Show Report":
        sg.popup("This is a report message.", title="Report")
    elif event == "Confirm Action":
        confirm = sg.popup_yes_no("Do you want to proceed?", title="Confirmation")
        if confirm == "Yes":
            sg.popup("Action confirmed.", title="Confirmation")

window.close()