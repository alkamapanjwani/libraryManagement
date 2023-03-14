from flask import Flask, render_template

# from markupsafe import escape

from flask_mysqldb import MySQL

# from

app = Flask(__name__)

app.secret_key = "flash_messages"

app.config["MYSQL_HOST"] = "localhost"
app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = "root"
app.config["MYSQL_DB"] = "library_db"

mysql = MySQL(app)


@app.route("/")
def index():
    return render_template("index.html")


# from member_cls import member_cls_bp
# app.register_blueprint(member_cls_bp, url_prefix='/member_cls')

from member import member_bp

app.register_blueprint(member_bp)


from author import author_bp

app.register_blueprint(author_bp)

from book import book_bp

app.register_blueprint(book_bp)

from setting import setting_bp

app.register_blueprint(setting_bp)

from issue_return_book import issue_return_book_bp

app.register_blueprint(issue_return_book_bp)

from transaction import transaction_bp

app.register_blueprint(transaction_bp)
# @app.route('/member') issue_return_book_model
# def member():
#     cur=mysql.connection.cursor()
#     cur.execute("SELECT * FROM member")
#     data = cur.fetchall()
#     cur.close()

#     return render_template('member.html',member=data)


if __name__ == "__main__":
    app.run(debug=True)

# @app.route("/name/<name>/")
# def hello_world(name):
#   return "<p>Hello, World Alkama!</p> " + str(1) + name +"test"+url_for('name',name='a')
#   with app.test_request_context():
#      print(url_for('index'))
