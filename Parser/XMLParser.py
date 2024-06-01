import xml.etree.ElementTree as ET

class XMLParser:
    
        def __init__(self):   # インスタンス生成時に自動的に呼ばれるメソッド
            pass
    
        # xmlの解析
        def XMLParser(self, xmlPath:str) -> dict[str, str]:
 
            tree = ET.parse(xmlPath)
            root = tree.getroot()

            root.tag
            root.attrib

            xmlDic = {}
            
            for child in root:
                atrb:str = child.get('name')            # type: ignore
                for gran in child:
                    altName:str = gran.get('name_alt')  # type: ignore
                    break
                if altName is not None:
                    xmlDic[atrb] = altName
                 
            return xmlDic        
                    
                    