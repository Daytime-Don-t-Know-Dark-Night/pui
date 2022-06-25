from DataBaseUtils import MysqlUtils

db = MysqlUtils()


def src():
    sql = """ select * from user """
    data = db.dingchao_db.getData(sql)
    print(data)


if __name__ == '__main__':
    src()
