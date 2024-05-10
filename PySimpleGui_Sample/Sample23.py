"""
進捗バー

進捗状況を視覚的に表示するためのウィジェットです。
タスクの進行状況を示すために使用します。
"""

import PySimpleGUI as sg

layout = [
    [sg.ProgressBar(100, orientation="h", size=(20, 15))],
    [sg.Button("Start")]
]
window = sg.Window("ProgressBar Widget Example", layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    if event == "Start":
        progress_bar = window["ProgressBar"]
        for i in range(1, 101):
            progress_bar.Update()
        sg.popup("Task completed!")

window.close()