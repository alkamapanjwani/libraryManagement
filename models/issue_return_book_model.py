from app import mysql

class issue_return_book_model():
  
   def get_issue_return_book_list(self):
        cur=mysql.connection.cursor()
        cur.execute("SELECT bi.book_issue_id, b.title, m.name,GROUP_CONCAT(a.name SEPARATOR '/ ') as author,"+
                    " bi.issue_date, bi.return_date, bi.is_returned_flag FROM book_issue bi inner join book b on b.book_id=bi.book_id"+
                    " inner join member m on m.member_Id=bi.book_id inner join book_auhor_trans bat on bat.book_id=b.book_id"+
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
        print(member_id)
        print(book_id)

        cur.execute("INSERT INTO book_issue (member_id, book_id) VALUES (%s, %s)",(member_id, book_id))
        book_issue_id=cur.lastrowid    
        print(book_issue_id) 
        cur.close()
        mysql.connection.commit()

      #   data=[book_details,book_author]
        return "Book Issued Successfully"
   