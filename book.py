from app import mysql
import app
import re
import urllib.request, json
from flask import Blueprint,render_template, request, redirect, url_for, flash
from models.book_model import book_model
from models.import_api_book_model import import_api_book_model
from models.author_model import author_model

book_model = book_model()
import_api_book_model= import_api_book_model()
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

@book_bp.route('/insert_update_book/<string:id_data>', methods=['POST','GET'])
def insert_update_book(id_data):
    author_list=author_model.getall()           
    if request.method=="POST":             
        title=request.form['title']
        isbn13=request.form['isbn13']
        qty=request.form['qty']
        author_selected_list = request.form.getlist('author')
        
        error = validate(title,isbn13,qty,author_selected_list,id_data)
        if error is None:
            try:        
                if id_data == '0':
                    flash(book_model.insert(title,isbn13,qty,author_selected_list))       
                else:
                    flash(book_model.update(title,isbn13,qty,author_selected_list,id_data))       

                return redirect(url_for('book_bp.book'))
            except Exception as error:
                print(error)
                return render_template('error_occured.html')
        else:
            flash(error)
            submit_type='Add'
            if id_data != '0': submit_type='Update' 
            print(author_list)
            print(type(author_list))
            print(author_selected_list)
            print(type(author_selected_list))
            return render_template('add_update_book.html', res={"id_data":id_data,"author_list": author_list, "author_selected_list": author_selected_list,
                                    "submit_type":submit_type, "title":title,"isbn13":isbn13,"qty":qty})
    else:         
        author_selected_list = []    
        submit_type='Add'
        title=''
        isbn13=''
        qty=''
        if id_data != '0': 
            submit_type='Update' 
            book_data, book_author=book_model.getbookbyid(id_data)
            # print(book_data[1])
            # author_selected_list=book_data[1]
            author_selected_list=list(map(str,list(zip(*book_author))[0]))
            # author_selected_list = list( map(str,book_author))
            book_details= book_data[0]
            print(book_details[0][0])
            # print(author_list)
            # print(author_selected_list)
            print(author_list)
            print(type(author_list))
            print(author_selected_list)
            print(type(author_selected_list))
            # print(book_details[0])
            title= book_details[0]
            isbn13=book_details[1]
            qty=book_details[2]

        return render_template('add_update_book.html', res={"id_data":id_data,"author_list": author_list, "author_selected_list": author_selected_list,
                                    "submit_type":submit_type, "title":title,"isbn13":isbn13,"qty":qty})
    
@book_bp.route('/delete_book/<string:id_data>', methods = ['GET'])
def delete_book(id_data):
    try:
        flash(book_model.delete(id_data)) 
        return redirect(url_for('book_bp.book'))
    except Exception as error:
        print(error)
        return render_template('error_occured.html')
    
@book_bp.route('/import_api_book', methods=['POST','GET'])
def import_api_book():
    if request.method=="POST":             
        title=request.form['title']
        count=request.form['count']
      
        #error = validate(title,count)
        error=None
        if error is None:
            try:   
                i=0  
                page=1
                booklist=[]
                bookCnt=int(count)
                while (i < bookCnt):                    
                    url = "https://frappe.io/api/method/frappe-library?title="+title+"&page="+str(page)
                    response = urllib.request.urlopen(url)
                    data = response.read()
                    dict = json.loads(data)
                    curBookList=dict.get('message')
                    if len(curBookList) > 0:
                        booklist=booklist+curBookList
                        i=len(booklist)
                        page=page+1
                    else: break
                # print(booklist)
                # print(type(booklist))
                # print(i)

                flash(import_api_book_model.insert(booklist,bookCnt))    
                return redirect(url_for('book_bp.book'))
            except Exception as error:
                print(error)
                return render_template('error_occured.html')
        else:
            flash(error) 
            return render_template('import_api_book.html',  res={"title":title,"count": count})

    else:         
        title=''
        count=''              
        return render_template('import_api_book.html', res={"title":title,"count": count})


regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'

def validate(title,isbn13,qty,authorlist,id_data):    
    error = None
    if not title:
        error = "title is required."
    elif not isbn13:
        error = "isbn13 is required."
    elif not qty:
        error = "quantity is required."
    elif not authorlist:
        error = "author is required."
    elif not (book_model.check_duplicate_isbn(isbn13,id_data)) == 0:
        error = "the isbn13 entered already exists in system."
    print(error)
        
    return error