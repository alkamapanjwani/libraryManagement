from app import mysql
from models.base_model import BaseModel

class author_model(BaseModel):

   def __init__(self):
      self.tablename='author'
      super().__init__(self.tablename)      
   
   def insert(self,name):
      cur=mysql.connection.cursor()
      cur.execute("INSERT INTO author (name) VALUES (%s)", (name,))
      mysql.connection.commit()
      return "Data Inserted Successfully"
   
   def insert_if_not_exists(self,name):
      cur=mysql.connection.cursor()
      cur.execute("SELECT author_id FROM author where name=%s", (name,))
      row = cur.fetchone()
      if row == None:
         cur.execute("INSERT INTO author (name) VALUES (%s)", (name,))
         author_id=cur.lastrowid
      else: author_id = row[0]
      mysql.connection.commit() 
      return author_id

   def update(self,name,id_data):
      cur=mysql.connection.cursor()
      cur.execute("UPDATE author SET name=%s  WHERE author_id=%s", (name, id_data))
      mysql.connection.commit()
      return "Data Updaeted Successfully"
  
   def delete(self,id_data):
      cur=mysql.connection.cursor()
      cur.execute("UPDATE author SET is_active_flag=0  WHERE author_id=%s", (id_data))
      #cur.execute("DELETE FROM member WHERE member_id=%s", (id_data))
      mysql.connection.commit()
      return "Record Has Been Deleted Successfully"