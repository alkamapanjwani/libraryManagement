from app import mysql

class BaseModel:

    def getall(self):
        cur=mysql.connection.cursor()
        cur.execute(f"SELECT * FROM {self.tablename}")
        data = cur.fetchall()
        cur.close()
        return data
    
    def __init__(self,tablename):
      self.tablename=  tablename

     
      