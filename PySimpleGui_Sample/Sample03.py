"""
ウィジェットの配置

PySimpleGUIでは、ウィンドウに配置するウィジェット（ボタン、テキスト、入力フィールドなど）を
シンプルな方法で指定できます。
例えば、以下のコードで「Hello, PySimpleGUI!」と表示するウィンドウを作成できます。
"""

import PySimpleGUI as sg

layout = [[sg.Text("Hello, PySimpleGUI!")], [sg.Button("OK")]]
window = sg.Window("My Window", layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == "OK":
        break

window.close()

"""
PysimpleGui入門
https://zenn.dev/torachi0401/articles/pysimplegui_articles
"""