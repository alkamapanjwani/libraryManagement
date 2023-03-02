from flask import Flask, render_template, request, redirect, url_for, flash
#from markupsafe import escape

from flask_mysqldb import MySQL

#from

app = Flask(__name__)

app.secret_key="flash_messages"

app.config['MYSQL_HOST']= 'localhost'   
app.config['MYSQL_USER']= 'root'
app.config['MYSQL_PASSWORD']= 'root'
app.config['MYSQL_DB']= 'library_db'

mysql=MySQL(app)

@app.route('/')
def index():
    cur=mysql.connection.cursor()
    cur.execute("SELECT * FROM member")
    data = cur.fetchall()
    cur.close()
   
    return render_template('index.html',member=data)

@app.route('/insert', methods=['POST'])
def insert():
    if request.method=="POST":
        flash("Data Inserted Successfully")
        name=request.form['name']
        email=request.form['email']
        phone=request.form['phone']

        cur=mysql.connection.cursor()
        cur.execute("INSERT INTO member (name, email, phone) VALUES (%s, %s, %s)",(name, email, phone))
        mysql.connection.commit()
        return redirect(url_for('index'))

@app.route('/update',methods=['POST','GET'])
def update():
    if request.method == 'POST':
        id_data = request.form['id']
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        cur = mysql.connection.cursor()
        cur.execute("UPDATE member SET name=%s, email=%s, phone=%s  WHERE member_id=%s", (name, email, phone, id_data))
        flash("Data Updated Successfully")
        mysql.connection.commit()
        return redirect(url_for('index'))

@app.route('/delete/<string:id_data>', methods = ['GET'])
def delete(id_data):
    flash("Record Has Been Deleted Successfully")
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM member WHERE member_id=%s", (id_data,))
    mysql.connection.commit()
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug=True)

#@app.route("/name/<name>/")
#def hello_world(name):
 #   return "<p>Hello, World Alkama!</p> " + str(1) + name +"test"+url_for('name',name='a')
 #   with app.test_request_context():
  #      print(url_for('index'))
