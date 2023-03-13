from app import mysql
from models.base_model import BaseModel

class member_model(BaseModel):

   def __init__(self):
      self.tablename='member'
      super().__init__(self.tablename)
      
   
   def insert(self,name,email,phone):
      cur=mysql.connection.cursor()
      cur.execute("INSERT INTO member (name, email, phone) VALUES (%s, %s, %s)",(name, email, phone))
      mysql.connection.commit()
      cur.close()
      return "Data Inserted Successfully"
   
   def update(self,name,email,phone,id_data):
      cur=mysql.connection.cursor()
      cur.execute("UPDATE member SET name=%s, email=%s, phone=%s  WHERE member_id=%s", (name, email, phone, id_data))
      mysql.connection.commit()
      cur.close()
      return "Data Updaeted Successfully"
  
   def delete(self,id_data):
      cur=mysql.connection.cursor()
      cur.execute("UPDATE member SET is_active_flag=0  WHERE member_id=%s", (id_data))
      #cur.execute("DELETE FROM member WHERE member_id=%s", (id_data))
      mysql.connection.commit()
      cur.close()
      return "Record Has Been Deleted Successfully"