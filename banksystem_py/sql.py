import pymysql
mysql=None
class SQLdata():
    sql=None
    def __init__(self):
        self.sql=None
    def connect(self):
        try:
            self.sql=pymysql.Connect(host='localhost', port=3306, user='root', password='MySQL@123',\
                                     database='dbtest', charset='utf8')
        except:
            print("error:连接db失败")
            return None
        return self.sql
    def close(self):
        self.sql.close()
        self.sql=None
if(mysql==None):
    mysql=SQLdata()
def getMySql():
    return mysql
