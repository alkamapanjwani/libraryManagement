from app import mysql
from models.base_model import BaseModel


class Setting_model(BaseModel):
    def __init__(self):
        self.tablename = "setting"
        super().__init__(self.tablename)

    def get_outstanding_debt(self):
        cur = mysql.connection.cursor()
        cur.execute(
            "select setting_value from setting where setting_name='outstanding_debt'"
        )
        data = cur.fetchone()[0]
        print(data)
        cur.close()
        return data

    def get_book_fees(self):
        cur = mysql.connection.cursor()
        cur.execute("select setting_value from setting where setting_name='book_fees'")
        data = cur.fetchone()[0]
        print(data)
        cur.close()
        return data

    def update(self, outstanding_debt, book_fees):
        cur = mysql.connection.cursor()
        cur.execute(
            "UPDATE setting SET setting_value=%s where setting_name='outstanding_debt'",
            (outstanding_debt,),
        )
        cur.execute(
            "UPDATE setting SET setting_value=%s where setting_name='book_fees'",
            (book_fees,),
        )

        mysql.connection.commit()
        cur.close()
        return "Data Updated Successfully"
