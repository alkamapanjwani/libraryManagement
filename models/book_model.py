from app import mysql
from models.base_model import BaseModel

class book_model(BaseModel):

   def __init__(self):
      self.tablename='book'
      super().__init__(self.tablename)
      
  
   def getbookwithauthor(self):
        cur=mysql.connection.cursor()
        cur.execute("SELECT b.book_id, b.title, GROUP_CONCAT(a.name SEPARATOR '/ ') as author, b.isbn13, b.totalqty FROM library_db.book b inner join book_auhor_trans bat "+
"on b.book_id=bat.book_id  "+
"inner join author a on a.author_id=bat.author_id  "+
"where b.is_active_flag=1 "+
"group by b.book_id, b.title, b.isbn13, b.totalqty")
        data = cur.fetchall() 
        cur.close()
        return data
   
   def insert(self,title,isbn13,qty,authorlist):
      cur=mysql.connection.cursor()
      cur.execute("INSERT INTO book (title, isbn13, totalqty) VALUES (%s, %s, %s)",(title, isbn13, qty))
      book_id=cur.lastrowid
      for author_id in authorlist:
        cur.execute("INSERT INTO book_auhor_trans (book_id,author_id) VALUES (%s,%s)",(book_id,author_id))
      mysql.connection.commit()
      return "Data Inserted Successfully"
   
   def update(self,name,email,phone,id_data):
      cur=mysql.connection.cursor()
      cur.execute("UPDATE member SET name=%s, email=%s, phone=%s  WHERE member_id=%s", (name, email, phone, id_data))
      mysql.connection.commit()
      return "Data Updaeted Successfully"
  
   def delete(self,id_data):
      cur=mysql.connection.cursor()
      cur.execute("UPDATE member SET is_active_flag=0  WHERE member_id=%s", (id_data))
      #cur.execute("DELETE FROM member WHERE member_id=%s", (id_data))
      mysql.connection.commit()
      return "Record Has Been Deleted Successfully"