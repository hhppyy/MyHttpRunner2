import time
import pymysql

dbinfo = {
    "host": "123.56.231.107",
    "user": "root",
    "password": "123456",
    "port": 3309
}


class DbConnect():
    def __init__(self, db_cof=dbinfo, database=""):
        self.db_cof = db_cof
        # 打开数据库连接
        self.db = pymysql.connect(database=database,
                                  cursorclass=pymysql.cursors.DictCursor,
                                  **db_cof)
        # 使用cursor()方式获取操作游标
        self.cursor = self.db.cursor()

    def select(self, sql):
        # SQL 查询语句
        # sql = "SELECT * FROM EMPLOYEE \
        #       WHERE INCOME > %s" % (1000)
        self.cursor.execute(sql)
        results = self.cursor.fetchall()
        return results

    def execute(self, sql):
        # SQL 删除、提交、修改语句
        # sql = "DELETE FROM EMPLOYEE WHERE AGE > %s" % (20)
        try:
            # 执行SQL语句
            self.cursor.execute(sql)
            # 提交修改
            self.db.commit()
        except:
            # 发生错误时回滚
            self.db.rollback()

    def close(self):
        # 关闭连接
        self.db.close()


def select_sql(sql):
    '''查询函数'''
    db = DbConnect(database="hrun")
    result = db.select(sql)
    db.close()
    return result


def execute_sql(sql):
    '''执行函数（新增、删除、修改）'''
    db = DbConnect(database="hrun")
    db.execute(sql)
    db.close()


def del_date(username):
    """
    hooks函数，查询用户如果存在就删除
    :param username:
    :return:
    """
    sel_sql = """select id,username,password,email,`status`,CAST(create_time AS CHAR) AS create_time,CAST(update_time AS CHAR) AS update_time from UserInfo where username='%s';""" % username
    del_sql = """DELETE from UserInfo WHERE username='%s';""" % username
    if select_sql(sel_sql):
        execute_sql(del_sql)
        print('%s已经清理' % username)
    else:
        print('%s未注册，请先注册' % username)


def sel_date(username):
    sel_sql = """select id,username,password,email,`status`,CAST(create_time AS CHAR) AS create_time,CAST(update_time AS CHAR) AS update_time from UserInfo where username='%s';""" % username
    if select_sql(sel_sql):
        print('%s注册成功' % username)


def sleep(n_secs):
    time.sleep(n_secs)
