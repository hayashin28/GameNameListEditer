import json


class JsonOutput:
    
    def __init__(self):   # インスタンス生成時に自動的に呼ばれるメソッド
        pass


    def JsonOutput(self, lplPath:str, xmlDic:dict, lplDic:dict):

        for items in lplDic['items']:
            
            if items['label'] in xmlDic.keys():
                items['label'] = xmlDic[items['label']]


        # JSONデータをファイルに書き込み
        with open(lplPath + '.json' , 'w', encoding='utf-8') as file:
            json.dump(lplDic, file, ensure_ascii=False, indent=4, sort_keys=True, separators=(',', ': '))