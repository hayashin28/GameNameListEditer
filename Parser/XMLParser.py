import shutil
import xml.etree.ElementTree as ET

class XMLParser:
    
        def __init__(self):   # インスタンス生成時に自動的に呼ばれるメソッド
            pass
    
        # xmlの解析
        def XMLParser(self, xmlPath:str, lplPath:str):
        
            shutil.copy(lplPath, lplPath+'.bk')
            # 既存ファイルの読み込み
            with open(lplPath, encoding='UTF-8') as reader:    
                data_lines = reader.read()
        
        
            tree = ET.parse(xmlPath)
            root = tree.getroot()

            root.tag
            root.attrib

            for child in root:
                atrb:str = child.get('name') # type: ignore
                for gran in child:
                    altName:str = gran.get('name_alt') # type: ignore
                    
                    if altName != None:
                        # 指定したファイルの文字列を置換する
                        data_lines = data_lines.replace(atrb, altName)

            # 3.同じファイル名で保存
            with open(lplPath, mode='w', encoding='UTF-8') as writer:    
                writer.write(data_lines)
                    
                    
                    
                    