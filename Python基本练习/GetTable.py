'''
测试机器内存有限，M2DB中存在许多非必要的表。
该程序从业务程序的配置文件中，获取到M2DB模块的表名。
再结合对应的建表语句脚本，优化M2DB的表数量。
时间 2021/2/23
'''

from typing import List
import re
import sys

# 第一步，获取表名
# 参数cfg_path表示文件的绝对路径
# 以列表的形式，返回获取到的表名
def get_tablename(cfg_path:str) -> List[str]:
    # 保存表名
    t_name = []
    # 保持匹配的字符串
    re_str = []
    
    table_id = 1

    print('配置文件路径',cfg_path)
    # 1、打开文件
    with open (cfg_path,'r+',encoding='utf8') as cfg_file:
        print('Open file successfully')
        # 逐行读取文件内容
        while True:
            content_line = cfg_file.readline()
            if content_line:
                # 正则匹配SQL语句中非表名部分
                # \s 匹配任意空白字符
                # .  匹配任意字符,除了换行符
                # 第一个正则项：\s+from.*\s+on，匹配以from开头，on结尾的字符串。
                #     from两边加上\s是分别是为了匹配换行符和from关键字后的空格
                # 第二个正则项：\s+on.*，匹配以from开头，where单词结尾的字符串。

                # 利用findall函数，返回符合的匹配项数据类型为列表
                name_list = re.findall(r'\s+from.*\s+on|\s+from.*\s+where\b',content_line)
                name_str = ' '.join(name_list)

                # 如果匹配成功，输出表名
                # 匹配的字符串样例,from TB_PRD_OFR on
                if name_str:
                    re_str.append(name_str)
                    # 除去from、where、on关键字，空格,where开头，on结尾的字符串
                    name_tab = re.sub(r'\s+where.*\bon|\s+from\s+|\s+on|\s+where','',name_str)
                    
                    # 放入列表
                    t_name.append(name_tab)
                    table_id += 1
            # 读取文件结束，退出while
            else :
                break

    return t_name

# 第二步，根据表名获取建表语句
def get_sql(sql_file:str,table_name:List[str]):
    # 表名去重
    table_name = list(set(table_name))

    # 打开sql文件
    with open(sql_file,'r+',encoding='utf8') as sql:
        # 一次读取所有内容
        content_sql = sql.read()
        # 匹配所有索引语句的正则表达式
        index_re_str =  r'create\s+index\s+.*?;'
        index_sql_list = re.findall(index_re_str,content_sql,re.I)
        # 转换为字符串
        index_sql_str = '\n'.join(index_sql_list)
        
        

        if content_sql:
            # 重新生成m2db脚本文件
            with open('new_m2db.sql','w+',encoding='utf8') as new_m2db_file:
                
                new_m2db_file.write('\n'.join(table_name) + '\n')
                for i_name in table_name:
                    
                    # 处理关联查询的表名
                    # 表与表之间关联，会存在','
                    if ',' in i_name:
                        complex_name_str = i_name.replace(',',' ')
                        # split返回值为字符串列表
                        complex_name_list = complex_name_str.split(' ')
                        # 无需去除表名的别称，因为匹配不上
                        for n in complex_name_list:
                            # 新表名重新推入列表table_name
                            table_name.append(n)

                    # 匹配建表sql的正则表达式为：create\s+table\s+{table_name}.*?;
                    table_re_str =  r'create\s+table\s+' + i_name + r'.*?;'
                     
                    # 匹配建表语句
                    create_sql_list = re.findall(table_re_str,content_sql,re.S|re.I)
                    
                    # 再用表名匹配索引
                    result_index_list = re.findall(r'.*\bat\s+' + i_name + r'.*?;',index_sql_str,re.I)
                    
                    # findall函数返回的是列表，这里转换为字符串
                    create_str = ''.join(create_sql_list)
                    result_index_str = '\n'.join(result_index_list)

                    # 匹配成功,结果写入文件new_m2db.sql
                    if create_str :
                        new_m2db_file.write(create_str + '\n' + result_index_str + '\n')
                print(r'new_m2db.sql新文件生成完毕！')

# main函数
def main(argv):
    # 根据业务程序配置文件，获取表名
    table_name = get_tablename(argv[1])                   

    # 根据表名，获取建表语句
    get_sql(argv[2],table_name)

    # 最后输出下表名
    print('表名：',table_name)             
                

            


if __name__ == '__main__':
    #config_file = r"C:\Users\lcy_yy\Documents\GitHub\Python\acct_m2db.xml"
    #sql_file = r"C:\Users\lcy_yy\Documents\GitHub\Python\m2db0_20210223.sql"
    # 最后输出下表名
    main(sys.argv)
    