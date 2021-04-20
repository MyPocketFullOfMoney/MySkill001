"""
主要用于操作sql配置文件
"""

from xml.dom.minidom import parse
import xml.dom.minidom
import re

class XmlFile:
    """获取sql配置文件元素和值的方法"""


    def get_xml_item(self,
    xml_file_path:str = r'C:\Users\lcy_yy\Documents\GitHub\Python\OOO\xmlfile\AcctItemIvpn_910.sql.xml',
    item_name:str = "sql",item_attribute:str = "name"
    ):
        """打开配置文件,返回对应的元素。
        
        参数：  
        xmlfilepath:配置文件路径;str类型  
        itemname:元素名称  
        itemattribute:元素属性
        """
        with xml.dom.minidom.parse(xml_file_path) as DomTree:
            # 获取配置文件根节点dcsql
            dcsql = DomTree.documentElement
            # 获取sql元素
            sql_item = dcsql.getElementsByTagName(item_name)
            # {sql_name:sql_str}
            sql_dict = {}
            # 打印sqlname
            for sql in sql_item:
                
                sql_name = sql.getAttribute(item_attribute)
                sql_str = re.sub(r'\s+','',sql.childNodes[0].data)
                sql_dict[sql_name] = sql_str

            print(sql_dict)
            return dcsql


    def getDataBase(self):
        """获取数据库连接实例"""
        pass

    def getSqlString(self,sqlname:str) -> str:
        """获取sql字符串"""
        pass

    def updateDataBase(self):
        """"更新数据库连接实例"""
        pass

if __name__ == "__main__":
    test = XmlFile()
    test.get_xml_item()

    
    
