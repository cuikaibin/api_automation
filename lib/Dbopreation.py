import pymysql
from lib import Config

class PyMysql(object):
    """
    初始化数据库
    """
    # 也可以继承 Connection 这里没有选择继承
    def __init__(self, data, database, databasename='test', **kwargs):
        if databasename == 'test':
            self.connect = pymysql.connect(
                host=data.db_host,  # 连接名
                port=int(data.db_port),  # 端口
                user=data.db_user,  # 用户名
                password=data.db_password,  # 密码
                charset=data.db_charset,  # 不能写utf-8 在MySQL里面写utf-8会报错
                # cursorclass=data["db_cursorclass"],  # 数据转换成字典格式
                database=database,  # 数据库库名
            )
        elif databasename == 'tech':
            print(data.tech_db_host,data.tech_db_port,data.tech_db_user,data.tech_db_password,data.tech_db_charset)
            self.connect = pymysql.connect(
                host=data.tech_db_host,  # 连接名
                port=int(data.tech_db_port),  # 端口
                user=data.tech_db_user,  # 用户名
                password=data.tech_db_password,  # 密码
                charset=data.tech_db_charset,  # 不能写utf-8 在MySQL里面写utf-8会报错
                # cursorclass=data["db_cursorclass"],  # 数据转换成字典格式
                database=database,  # 数据库库名
            )
        else:
            print('数据库未定义')
            pass

    def query(self, sql, args=None, fetchone=False, end=True, onprint=True):
        """
        :param sql : sql字符串 eq "select * from course_rights where user_id = '{0}'"
        :param args : sql参数化数据参数，可迭代对象，元组、列表、字典都可以
        :param fetchone ：是否查询一条数据，True 返回查询第一条数据，返回类型字典，False 返回查询全部数据，返回类型 列表
        :param end : 是否销毁连接，True销毁连接，False不销毁
        :param onprint : 是否打印执行sql，True打印，False不打印
        """

        try:
            result = None
            with self.connect.cursor(cursor=pymysql.cursors.DictCursor) as cursor:
                # 返回响应结果数
                sql_0 = self.sql_args_2_sql(sql, args)
                if onprint:
                    print('执行sql：%s' % sql_0)
                effect_row = cursor.execute(sql_0)
                if fetchone:
                    result = cursor.fetchone()
                else:
                    result = cursor.fetchall()
        except Exception as e:
            print(e)
        finally:
            #结束关闭连接
            if end:
                self.connect.close()
            else:
                pass
        return result

    def execute(self, sql, args=None, response=False, end=True, onprint=True):
        """
        :param sql : sql字符串 eq "select * from course_rights where user_id = '{0}'"
        :param args : sql参数化数据参数，可迭代对象，元组、列表、字典都可以
        :param response ：是否返回执行结果，True 返回执行结果，False 不返回执行结果
        :param end : 是否销毁连接，True销毁连接，False不销毁
        :param onprint : 是否打印执行sql，True打印，False不打印
        """

        try:
            result = None
            with self.connect.cursor(cursor=pymysql.cursors.DictCursor) as cursor1:
                sql_0 = self.sql_args_2_sql(sql, args)
                if onprint:
                    print('执行sql：%s' % sql_0)
                effect_row = cursor1.execute(sql_0)
                if response:
                    result = cursor1.fetchall()

            # connection is not autocommit by default. So you must commit to save your changes.
            self.connect.commit()
        except Exception as e:
            print(e)
            # error rollback
            self.connect.rollback()
        finally:
            if end:
                self.connect.close()
            else:
                pass
        if response:
            return result

    def sql_args_2_sql(self, sql, args):
        '''
        fix  issue  %d format: a number is required, not str
        :param sql: sql语句
        :param args: 格式化参数
        :return: 组合之后的sql语句
        '''
        if args is None:
            return sql
        if sql.find('%') > -1:
            return sql % args
        elif sql.find('{') > -1:
            if type(args) is dict:
                return sql.format(**args)
            else:
                return sql.format(*args)
        return sql



if __name__ == '__main__':
    conf = Config.Config()
    # db = PyMysql(conf, "course_rights_test")
    # sql = "select * from course_rights where user_id = '{0}' "
    # arg = (200407,)
    # dict_result = db.query(sql=sql, args=arg, fetchone=False, end=False)
    # print(dict_result)
    # print(db.query(sql="select * from course_rights where user_id =%s", args=('200407',), fetchone=False, end=False))
    # print(db.query(sql="select * from course_rights where user_id = '{user_id}'", args={'user_id':'200407'}, fetchone=False))
    db1 = PyMysql(conf, "monkey_tech","tech")
    sql1 = "SELECT id,user_id,credits,create_time,update_time FROM xes_user_asset WHERE id = %s"
    re= db1.query(sql=sql1, args=1091, fetchone=False, end=False)
    print(len(re),re)

