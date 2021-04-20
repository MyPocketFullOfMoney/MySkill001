import re 
import sys
import os
from xml.dom.minidom import parse
import xml.dom.minidom

"""
重写简化M2DB表的方法
时间：2021/3/27

计划：unittest测试安排上
"""

class SimpleTable:
    def __init__(self):
        """初始化函数"""
        pass

    def open_xml_file(self,xml_file_path:str):
        """从配置文件中获取SQL语句,返回SQL语句和表名"""
        
        m2db_inst_name = []
        xml_tablename = []
        xml_sql_str = []

        # 打开xml文档
        dom_tree = xml.dom.minidom.parse(xml_file_path)

        # 获取根节点
        root_node= dom_tree.documentElement 

        # 获取<dbinst>元素
        dbinst_items = root_node.getElementsByTagName("db")
        
        for dbinst in dbinst_items:

            category = dbinst.getAttribute("category")

            # 判断数据库实例category属性是否为UM2DB,获取数据库实例名称
            if "UM2DB" == category:
                m2db_inst_name.append(dbinst.getAttribute("name"))

        module_items = root_node.getElementsByTagName("module")

        # 查找所有module模块中的sql语句，但只获取m2db_inst_name中的sql语句
        for module in module_items:

            if module.getAttribute("db") in m2db_inst_name:
                sql_items = module.getElementsByTagName("sql")
                for sql in sql_items:
                    if sql.hasAttribute("sub"):
                        sub_list = sql.getAttribute("sub").split(',')
                    # 美化sql语句，去除字符串前后的空白字符
                    sqlstr = re.sub(r"^\s+|\s+$","",sql.childNodes[0].data,flags=re.I)
                    xml_sql_str.append(sqlstr)

                    # 获取表名
                    # 第一种情况，sql语句单表查询
                    table_mid_name = re.findall(r"\bfrom\s+[\w+\[\]@]+",sqlstr,flags=re.I)
                    table_name = re.sub(r"from\s+","",table_mid_name[0],flags=re.I)
                    # SQL存在参数需要替换
                    if "@" in table_name and len(sub_list) >= 1:
                        for i_sub in sub_list:
                            xml_tablename.append(table_name.replace("[@]",i_sub)) 
                    else:
                        xml_tablename.append(table_name)
        return xml_tablename



    def open_m2db_file(self,m2db_file_path:str):
        """从M2DB文件中获取表名，建表语句"""

        m2db_dict = {}

        with open(m2db_file_path,'r+',encoding='utf8') as m2db_file_stream:
            m2db_conten = m2db_file_stream.read()
            m2db_conten_list = m2db_conten.split(";")

            for i_m2db in m2db_conten_list:
                re_str = r"(?<=table)\s+[\w+\[\]@]+"
                m2db_table_name = self.get_table_name(re_str,i_m2db)

                if m2db_table_name:
                    m2db_table_name_key = re.sub(r"\s+","",m2db_table_name[0])

                    m2db_dict[m2db_table_name_key] = i_m2db
                    
            return m2db_dict
                

    def write_file(self):
        pass

    def get_table_name(self,re_str:str,target_sqlstr):
        table_mid_name = re.findall(re_str,target_sqlstr,flags=re.I)
        return table_mid_name
        
