"""
popup_get_file(
    message,
    title = None,
    default_path = "",
    default_extension = "",
    save_as = False,
    multiple_files = False,
    file_types = (('ALL Files', '*.*'),),
    no_window = False,
    size = (None, None),
    button_color = None,
    background_color = None,
    text_color = None,
    icon = None,
    font = None,
    no_titlebar = False,
    grab_anywhere = False,
    keep_on_top = False,
    location = (None, None),
    initial_folder = None,
    image = None,
    files_delimiter = ";",
    modal = True
)
"""
"""
名前	タイプ	意味
message	str	表示するメッセージ
title	str	ウィンドウタイトル
default_path	str	開始点としてユーザーに表示するパス（入力フィールドに入力）
default_extension	str	ユーザーが拡張子を入力していない場合は、これをファイル名に追加します（saveasダイアログでのみ使用されます）
save_as	bool	Trueの場合、上書きする前に確認する「名前を付けて保存」ダイアログが表示されます
multiple_files	bool	Trueの場合、「;」で返される複数のファイルを選択できます。各ファイル名の間
file_types	タプル[タプル[str、str]]	ワイルドカードを使用して表示する拡張機能のリスト。すべてのファイル（デフォルト）=（（ “ALL Files”、 ” 。 “）、）
no_window	bool	Trueの場合、PySimpleGUIウィンドウは表示されません。代わりに、tkinterダイアログのみが表示されます
size	（int、int）	InputText要素の（幅、高さ）
button_color	タプル[str、str]またはstr	ボタンの色（テキスト、背景）
background_color	str	ウィンドウ全体の背景色
text_color	str	テキストの色
icon	バイトまたはstr	ウィンドウのアイコンに使用されるファイル名またはbase64文字列
font	strまたはTuple [str、int]	フォントファミリー、サイズなどを指定します
no_titlebar	bool	Trueの場合、タイトルバーは表示されません
grab_anywhere	bool	Trueの場合、ウィンドウを移動するためにどこでもつかむことができます（デフォルト= False）
keep_on_top	bool	Trueの場合、ウィンドウは現在のすべてのウィンドウの上に残ります。
location	タプル[int、int]	ウィンドウの左上隅の位置
initial_folder	str	ブラウジングを開始するファイルシステム内の場所
image	strまたはbytes	ポップアップウィンドウの上部に含める画像
files_delimiter	str	複数のファイルが選択されたときにファイル間に配置する文字列。通常は、”;”
modal	bool	Trueの場合、ポップアップはモーダルウィンドウのように動作します。他のすべてのウィンドウは、このウィンドウが閉じられるまで動作しません。デフォルト= True
"""
from Dialog.XMLSelecterDialog import XMLSelecterDialog
from Dialog.LPLSelecterDialog import LPLSelecterDialog
import PySimpleGUI as sg


#先程確認して決めたテーマカラーをsg.themeで設定
sg.theme('Dark Brown')

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
        window.refresh()                # 画面更新
        
        
    elif event == 'LPLBTN':
        pass

window.close()