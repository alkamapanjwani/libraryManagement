from app import mysql


class book_stock_model:
    def get_available_book_qty(self, book_id):
        cur = mysql.connection.cursor()
        cur.execute(
            "select (ifnull(b.totalqty,0)-ifnull((count(bi.book_issue_id)),0)) avlbBook from book b "
            + "left join book_issue bi on bi.book_id=b.book_id and bi.is_returned_flag='no' where b.book_id=%s",
            (book_id,),
        )
        #      " order by tr    ansaction_id desc"
        data = cur.fetchone()[0]
        cur.close()
        return data
