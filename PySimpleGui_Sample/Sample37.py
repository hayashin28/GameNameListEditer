"""
matplotlibで作成したグラフをレイアウトに埋め込む方法

PySimpleGUIを使用して作成したGUIに、matplotlibで作成したグラフを埋め込む方法について説明します。
"""

import PySimpleGUI as sg
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

layout = [
    [sg.Text("Embedded Matplotlib Graph Example")],
    [sg.Canvas(size=(400, 300), key="-CANVAS-")],
    [sg.Button("Exit")]
]

window = sg.Window("Embedded Matplotlib Graph Example", layout)

# Matplotlibのグラフを作成
fig, ax = plt.subplots()
ax.plot([0, 1, 2, 3, 4], [0, 1, 4, 9, 16])
canvas_elem = FigureCanvasTkAgg(fig, window["-CANVAS-"].Widget)
canvas_elem.get_tk_widget().pack()

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break

window.close()