from app import mysql
from models.transaction_model import transaction_model
from models.setting_model import Setting_model

transaction_model = transaction_model()
Setting_model = Setting_model()

class issue_return_book_model():
  
   def get_issue_return_book_list(self):
        cur=mysql.connection.cursor()
        cur.execute("SELECT bi.book_issue_id, b.title, m.name,GROUP_CONCAT(a.name SEPARATOR '/ ') as author,"+
                    " bi.issue_date, bi.return_date, bi.is_returned_flag FROM book_issue bi inner join book b on b.book_id=bi.book_id"+
                    " inner join member m on m.member_Id=bi.member_id inner join book_auhor_trans bat on bat.book_id=b.book_id"+
                    " inner join author a on a.author_id=bat.author_id group by bi.book_issue_id, b.title, m.name, bi.issue_date, bi.return_date")
        data = cur.fetchall() 
        cur.close()
        return data
   
   def mark_return(self,id_data):
      cur=mysql.connection.cursor()
      cur.execute("UPDATE book_issue SET is_returned_flag='yes'  WHERE book_issue_id=%s", (id_data,))
      #cur.execute("DELETE FROM member WHERE member_id=%s", (id_data))
      mysql.connection.commit()
      cur.close()

      return "Book Marked as Returned Successfully"

   def mark_issue(self,member_id,book_id):
        cur=mysql.connection.cursor()        
        cur.execute("INSERT INTO book_issue (member_id, book_id) VALUES (%s, %s)",(member_id, book_id))
        book_issue_id=cur.lastrowid  
        transaction_model.insert_dr(member_id,Setting_model.get_book_fees(),book_issue_id,'Book Issued',cur)
        print(book_issue_id)
        print(Setting_model.get_book_fees())
        mysql.connection.commit()
        cur.close()   

      #   data=[book_details,book_author]
        return "Book Issued Successfully"
   