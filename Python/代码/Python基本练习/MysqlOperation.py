'''
利用pymysql模块连接Mysql
时间:2021/2/28
'''

import pymysql

# 打开数据库连接
# 数据库的ip地址，账号，密码，数据库名称
my_db = pymysql.connect(host="localhost",user="root",password="123456",database="data_li")

# 创建一个游标对象
with  my_db.cursor() as my_cursor:

    # 先创建表EMPLOYEE
    creat_str = '''CREATE TABLE IF NOT EXISTS  EMPLOYEE(
                    FIRST_NAME CHAR(20) NOT NULL,
                    LAST_NAME CHAR(20),
                    AGE INT,
                    SEX CHAR(1),
                    INCOME FLOAT
                    ) '''
    
    # 使用execute()方法执行SQL
    my_cursor.execute(creat_str)
    
    print('表EMPLOYEE是否存在：',my_cursor.execute("SHOW TABLES LIKE 'EMPLOYEE' "))

    # SQL插入语句
    insert_str = '''INSERT INTO EMPLOYEE(FIRST_NAME,LAST_NAME,AGE,SEX,INCOME)
                    VALUES (%s,%s,%s,%s,%s )
                 '''
    insert_value = ['Mac','Bigbig',20,'M',9999]
    try:
        my_cursor.execute(insert_str,insert_value)
        # 提交！！！
        my_db.commit()
    except Exception as error:
        print(error)
        # 发生异常，则回滚
        my_db.rollback()

    # SQL 查询语句
    select_str = '''SELECT * FROM EMPLOYEE'''
    my_cursor.execute(select_str)
    # 获取所有记录
    results = my_cursor.fetchall()
    print(results[0])

