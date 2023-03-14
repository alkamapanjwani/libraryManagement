from app import mysql


class BaseModel:
    def getall(self):
        cur = mysql.connection.cursor()
        cur.execute(f"SELECT * FROM {self.tablename} where is_active_flag=1")
        data = cur.fetchall()
        cur.close()
        return data

    def __init__(self, tablename):
        self.tablename = tablename
