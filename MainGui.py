from Dialog.XMLSelecterDialog import XMLSelecterDialog
from Dialog.LPLSelecterDialog import LPLSelecterDialog
from Parser.XMLParser import XMLParser
from Parser.LPLParser import LPLParser
import PySimpleGUI as sg


#テーマカラーをsg.themeで設定
sg.theme('NeutralBlue') # 'Dark Brown'

#sg.Frameでフレームを定義
#フレーム1(中はからっぽ、フレームサイズだけ指定)
frame1 = sg.Frame('',
    [] , size=(500, 700) #幅,高さ
)

#フレーム2(中はからっぽ、フレームサイズだけ指定)
frame2 = sg.Frame('',
    [] , size=(500, 700) #幅,高さ
)

#全体レイアウト
"""
レイアウトの中に記述する[]が「1行」を表している
今回はframe1と2を横に並べるので、同じ[]の中に記述する
"""
frame1 = [
    #以下[]で1行の扱いになる。カンマ区切りで横に部品を並べられる
    [
        sg.Text('XMLファイルを選択', key='XMLTEXT')
    ],
    [
        sg.Input(key='XMLPATH', readonly=True), sg.Button('ボタン', key='XMLBTN')
    ],
]

frame2 = [
    #以下[]で1行の扱いになる。カンマ区切りで横に部品を並べられる
    [
        sg.Text('LPLファイルを選択', key='LPLTEXT')
    ],
    [
        sg.Input(key='LPLPATH', readonly=True), sg.Button('ボタン', key='LPLBTN')
    ],
]

layout = [
    [
        sg.Frame('',frame1),
    ],
    [
        sg.Frame('',frame2),
    ],
    [
        sg.Button('置換実行', disabled=False, key='REPBTN'),
    ],
]

#GUIタイトルと全体レイアウトをのせたWindowを定義する。画面サイズは省略OK
#resizableでWindowサイズをマウスで変更できるようになる
window = sg.Window('', layout, resizable=False)
window.finalize()

#GUI表示実行部分
while True:
    # ウィンドウ表示
    event, values = window.read()

    #クローズボタンの処理
    if event in (sg.WIN_CLOSED, event is None):
        break
    
    elif event == 'XMLBTN':
        instance = XMLSelecterDialog()
        path = instance.XMLSelecterDialog()        
        window['XMLPATH'].Update(path)  # テキスト追記 # type: ignore 
                   
    elif event == 'LPLBTN':
        instance = LPLSelecterDialog()
        path = instance.LPLSelecterDialog()
        window['LPLPATH'].Update(path)  # テキスト追記 # type: ignore

    elif event == 'REPBTN':
        xmlPath = values['XMLPATH']
        lplPath = values['LPLPATH']
        
        instance = XMLParser()
        xmlDic = instance.XMLParser(xmlPath)
   
        instance = LPLParser()
        lplDic = instance.LPLParser(lplPath)                   
   
    window.refresh()                    # 画面更新

window.close()