from app import mysql
from models.base_model import BaseModel


class book_model(BaseModel):
    def __init__(self):
        self.tablename = "book"
        super().__init__(self.tablename)

    def getbookwithauthor(self):
        cur = mysql.connection.cursor()
        cur.execute(
            "SELECT b.book_id, b.title, GROUP_CONCAT(a.name SEPARATOR '/ ') as author, b.isbn13, b.totalqty FROM book b inner join book_auhor_trans bat "
            + "on b.book_id=bat.book_id  "
            + "inner join author a on a.author_id=bat.author_id  "
            + "where b.is_active_flag=1 "
            + "group by b.book_id, b.title, b.isbn13, b.totalqty"
        )
        data = cur.fetchall()
        cur.close()
        return data

    def getbookbyid(self, id_data):
        cur = mysql.connection.cursor()
        cur.execute(
            "SELECT b.title, b.isbn13, b.totalqty FROM book b where b.book_id=%s",
            (id_data,),
        )
        book_details = cur.fetchall()
        cur.execute(
            "SELECT a.author_id FROM book_auhor_trans b inner join author a on a.author_id=b.author_id "
            + " where b.book_id=%s",
            (id_data,),
        )
        book_author = cur.fetchall()
        cur.close()
        #   data=[book_details,book_author]
        return book_details, book_author

    def insert(self, title, isbn13, qty, authorlist):
        cur = mysql.connection.cursor()
        cur.execute(
            "INSERT INTO book (title, isbn13, totalqty) VALUES (%s, %s, %s)",
            (title, isbn13, qty),
        )
        book_id = cur.lastrowid
        for author_id in authorlist:
            cur.execute(
                "INSERT INTO book_auhor_trans (book_id,author_id) VALUES (%s,%s)",
                (book_id, author_id),
            )
        mysql.connection.commit()
        cur.close()
        return "Data Inserted Successfully"

    def update(self, title, isbn13, qty, authorlist, id_data):
        cur = mysql.connection.cursor()
        cur.execute(
            "UPDATE book SET title=%s, isbn13=%s, totalqty=%s  WHERE book_id=%s",
            (title, isbn13, qty, id_data),
        )
        sql = (
            "DELETE FROM book_auhor_trans where book_id=%s and "
            + "author_id NOT IN (%s)"
        )
        in_ids = ", ".join(map(lambda x: "%s", authorlist))
        print(in_ids)
        sql = sql % ("%s", in_ids)
        print(in_ids)
        params = []
        params.append(id_data)
        params.extend(authorlist)
        print(sql)
        print(tuple(params))
        cur.execute(sql, tuple(params))

        for author_id in authorlist:
            cur.execute(
                "INSERT INTO book_auhor_trans (book_id,author_id) SELECT %s,%s WHERE NOT EXISTS ( SELECT * FROM book_auhor_trans "
                + " WHERE book_id =%s AND author_id = %s)",
                (id_data, author_id, id_data, author_id),
            )
        mysql.connection.commit()
        cur.close()
        return "Data Updated Successfully"

    def delete(self, id_data):
        cur = mysql.connection.cursor()
        cur.execute("UPDATE book SET is_active_flag=0  WHERE book_id=%s", (id_data,))
        # cur.execute("DELETE FROM member WHERE member_id=%s", (id_data))
        mysql.connection.commit()
        cur.close()
        return "Record Has Been Deleted Successfully"

    def check_duplicate_isbn(self, isbn13, id_data):
        cur = mysql.connection.cursor()
        cur.execute(
            "SELECT COUNT(*) FROM book where isbn13=%s and book_id!=%s",
            (isbn13, id_data),
        )
        isbn_count = cur.fetchone()[0]
        mysql.connection.commit()
        cur.close()
        return isbn_count

    def update_qty_isbn13(self, isbn13):
        cur = mysql.connection.cursor()
        cur.execute("UPDATE book SET totalqty=totalqty+1 where isbn13=%s", (isbn13,))
        update_count = cur.rowcount
        mysql.connection.commit()
        cur.close()
        return update_count
