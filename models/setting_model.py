from app import mysql
from models.base_model import BaseModel

class Setting_model(BaseModel):

   def __init__(self):
      self.tablename='setting'
      super().__init__(self.tablename)
      
  
   def get_outstanding_debt(self):
        cur=mysql.connection.cursor()
        cur.execute("select setting_value from setting where setting_name='outstanding_debt'")
        data = cur.fetchone()[0]
        print(data)
        cur.close()
        return data

   def update_outstanding_debt(self,outstanding_debt):
      cur=mysql.connection.cursor()
      cur.execute("UPDATE setting SET setting_value=%s where setting_name='outstanding_debt'",(outstanding_debt,))
      mysql.connection.commit()
      return "Data Updated Successfully"