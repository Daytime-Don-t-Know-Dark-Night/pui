"""
@desc 数据库操作方法
@auth dingc
@date 2022-06-25 12:17
"""

import pymysql
import logging as log
import pandas as pd
import time


class MysqlOperation:

    def __init__(self, host, user, password, db, port=3306):
        # TODO:进行修改, 不使用 try catch
        try:
            self.conn = pymysql.connect(host=host, user=user, passwd=password, db=db, charset='utf8mb4', port=port)
            self.cursor = self.conn.cursor()
        except Exception as e:
            log.info(e)

    def getData(self, sql):
        """
        :param sql:
        :return: tuple
        """
        self.cursor.execute(sql)
        # 返回多条记录
        result = self.cursor.fetchall()
        return result


