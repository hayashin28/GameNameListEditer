"""
ButtonMenu

ボタンをクリックした際にメニューを表示するためのウィジェットです。
特定のアクションを選択する際に便利です。
"""

import PySimpleGUI as sg

layout = [
    [sg.ButtonMenu("Options", menu_def=[
        ["Option 1", "Option 2", "Option 3"],
        ["Option 4", "Option 5", "Option 6"]
    ])],
    [sg.Button("Submit")]
]
window = sg.Window("ButtonMenu Widget Example", layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    if event == "Submit":
        sg.popup("Submit button clicked!")

window.close()