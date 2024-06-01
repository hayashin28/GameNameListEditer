import json
import shutil

class LPLParser:
    
    def __init__(self):   # インスタンス生成時に自動的に呼ばれるメソッド
        pass

    # plp(json)の解析
    def LPLParser(self, lplPath:str):

        shutil.copy(lplPath, lplPath + '.bk')
        # 既存ファイルの読み込み
        with open(lplPath, encoding='UTF-8') as reader:    
            data_lines = reader.read()
