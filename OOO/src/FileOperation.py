"""
主要用于操作sql配置文件
"""

from xml.dom.minidom import parse
import xml.dom.minidom

class XmlFile:
    """获取sql配置文件值得方法"""
    def openXmlFile(self,xmlfilepath:str = r'./xmlfile'):
        """打开配置文件,返回对应的元素"""
        with xml.dom.minidom.parse(xmlfilepath) as DomTree:
            RootNode = DomTree.documentElement
            return RootNode


    def getDataBase(self):
        """获取数据库连接实例"""
        pass

    def getSqlString(self):
        """获取sql字符串"""
        pass
    def updateDataBase(self):
        """"更新数据库连接实例"""
        pass
