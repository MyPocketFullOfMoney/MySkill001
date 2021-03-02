'''
前面通过正则表达式获取到了表的名字，但范围并不好控制。
所以这次希望通过先解析xml文件，获取到对应的sql语句，然后从sql语句匹配出表的名字
时间：2021/3/2
'''

from xml.dom.minidom import parse
import xml.dom.minidom
import re 

# 使用mindom解析器打开xml文档
DOMTree = xml.dom.minidom.parse('mon_acct.xml')

RootNode = DOMTree.documentElement

# 获取所有<module>元素
module_db = RootNode.getElementsByTagName('module')

for module_v in module_db:

    # 判断模块的属性值
    if 'ocsm2db_bill' == module_v.getAttribute('name'):
        sql_str_list = []
        # 获取模块中的所有<sql>元素
        sql_coll = module_v.getElementsByTagName('sql')
        # sql节点存在sql_coll
        for sql_node in sql_coll:
            # 获取sql元素的值，并替换字符串前后的空白字符
            sql_value = re.sub(r'^\s+|\s+$','',sql_node.childNodes[0].data)
            # 获取到select语句
            sql_str_list.append(sql_value)

            

# 接下来还是要通过正则匹配表名 - -||       
print('\n'.join(sql_str_list))

    