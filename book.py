from app import mysql
import app
import re
from flask import Blueprint,render_template, request, redirect, url_for, flash
from models.book_model import book_model

book_model = book_model()

from models.author_model import author_model

author_model = author_model()

book_bp = Blueprint('book_bp', __name__, url_prefix="/book")

@book_bp.route('/')
def book():
    try:
        # cur=mysql.connection.cursor()
        # cur.execute("SELECT * FROM member")
        # data = cur.fetchall()
        # cur.close()
        data=book_model.getbookwithauthor()
        return render_template('book.html',book=data)
    except Exception as error:
        print(error)
        return render_template('error_occured.html')

@book_bp.route('/insert_book', methods=['POST','GET'])
def insert_book():
    if request.method=="POST":            
        title=request.form['title']
        isbn13=request.form['isbn13']
        qty=request.form['qty']
        authorlist = request.form.getlist('author')
        error = validate(title,isbn13,qty,authorlist)
        if error is None:
            try:        
                flash(book_model.insert(title,isbn13,qty,authorlist))               
                return redirect(url_for('book_bp.book'))
            except Exception as error:
                print(error)
                return render_template('error_occured.html')
        else:
            flash(error)
            return redirect(url_for('book_bp.book'))
    else:
        author_list=author_model.getall()
        return render_template('add_update_book.html',res={"author_list": author_list, "product_list": author_list,"visible":True})
    


@book_bp.route('/update_book',methods=['POST','GET'])
def update_book():
    if request.method=="POST":
        id_data = request.form['id']            
        name=request.form['name']
        email=request.form['email']
        phone=request.form['phone']
        error = validate(name,email,phone)
        if error is None:
            try:        
                flash(book_model.update(name,email,phone,id_data)) 
                return redirect(url_for('book_bp.book'))
            except Exception as error:
                print(error)
                return render_template('error_occured.html')
        else:
            flash(error)
            return redirect(url_for('book_bp.book'))



@book_bp.route('/delete_book/<string:id_data>', methods = ['GET'])
def delete_book(id_data):
    try:
        flash(book_model.delete(id_data)) 
        return redirect(url_for('book_bp.book'))
    except Exception as error:
        return render_template('error_occured.html')
    
regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'

def validate(title,isbn13,qty,authorlist):    
    error = None
    if not title:
        error = "title is required."
    elif not isbn13:
        error = "isbn13 is required."
    elif not qty:
        error = "quantity is required."
    elif not authorlist:
        error = "author is required."
    return error