from app import mysql
from collections import deque

class transaction_model():
  
   def get_transaction_member_list(self,member_id):
        cur=mysql.connection.cursor()
        cur.execute("SELECT transaction_id,date_inserted,comment,dr_amount,cr_amount from transaction where member_id=%s",(member_id,))
        #      " order by tr    ansaction_id desc"
        data = cur.fetchall() 
        cur.close()
        translist=self.calculateAmount(data)
        return translist
   
   def calculateAmount(self,data):
        translist=[]
        amount=0
        for trans in data:
            transaction_id=trans[0]
            date_inserted=trans[1]
            comment=trans[2]
            dr_amount=trans[3]
            cr_amount=trans[4]
            amount=int(amount) + int(dr_amount) - int(cr_amount)
            transDict={"transaction_id":transaction_id,"date_inserted":date_inserted,"comment":comment,"dr_amount":dr_amount,
                       "cr_amount":cr_amount,"amount":amount}
            translist = deque(translist)
            translist.appendleft(transDict)
            translist = list(translist)
            #translist.append(transDict)
        return translist

   def insert_dr(self,member_id,dr_amount,book_issue_id,comment,cur):
        cur.execute("INSERT INTO transaction (member_id, dr_amount, book_issue_id,comment) VALUES (%s, %s,%s, %s)",
                    (member_id, dr_amount, book_issue_id, comment))       
        return "Record Inserted Successfully"    
   
   def insert_cr(self,member_id,cr_amount,comment):
        cur=mysql.connection.cursor() 
        cur.execute("INSERT INTO transaction (member_id, cr_amount, comment) VALUES (%s, %s, %s)",
                    (member_id, cr_amount, comment))
        mysql.connection.commit()
        cur.close()
        return "Record Inserted Successfully"    
    
   def get_amount_payable_member(self,member_id):
        cur=mysql.connection.cursor()
        cur.execute("select ifnull((sum(dr_amount)-sum(cr_amount)),0) as amtPayable from transaction where member_id=%s",(member_id,))
        #      " order by tr    ansaction_id desc"
        data = cur.fetchone()[0]
        cur.close()
        return data