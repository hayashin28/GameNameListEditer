import os
import json
import shutil

class LPLParser:
    
    def __init__(self):   # インスタンス生成時に自動的に呼ばれるメソッド
        pass

    # plp(json)の解析
    def LPLParser(self, lplPath:str) -> dict:
      
        i:int = 1

        while True:
            
            if os.path.isfile(lplPath + str(i) + '.bk'):
                i += 1
            else:
                break

        # 既存ファイルのバックアップ
        shutil.copy(lplPath, lplPath + str(i) + '.bk')
        # 既存ファイルの読み込み
        lplData = open(lplPath, mode='r', encoding='UTF-8')
        lplJson = json.load(lplData)

        return lplJson       