import pymysql


class MysqlDBDriver(object):
    '创建MySQL连接，利用上下文管理连接'

    def __init__(self, m_host, m_user, m_pwd, m_db):
        setting = {
            'host': m_host,
            'user': m_user,
            'password': m_pwd,
            'database': m_db
        }
        # 创建连接
        self.db_con = pymysql.connect(**setting)

        # 获取游标
        self.db_cur = self.db_con.cursor()

    # 返回游标
    def __enter__(self):
        return self.db_cur

    def __exit__(self, exc_type, exc_val, exc_tb):

        if exc_type:
            print(exc_val)
            self.db_con.rollback()
            print('发生异常，回滚数据！')
            return True
        else:
            # 关闭前先提交
            self.db_con.commit()

        # 关闭游标
        self.db_cur.close()

        # 关闭数据库连接
        self.db_con.close()


with MysqlDBDriver('localhost','root','123456','data_li') as li_cur:
    li_cur.execute('select * from aaa')
    result_tuple = li_cur.fetchall()
    print('结果：')
    print(result_tuple)

print('结束!')
