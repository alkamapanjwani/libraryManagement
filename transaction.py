from app import mysql
import app
import re
import urllib.request, json
from flask import Blueprint,render_template, request, redirect, url_for, flash
from models.transaction_model import transaction_model
from models.book_model import book_model
from models.member_model import member_model

transaction_model = transaction_model()
book_model = book_model()
member_model = member_model()

transaction_bp = Blueprint('transaction_bp', __name__, url_prefix="/transaction")

@transaction_bp.route("/", methods=['POST','GET'])
@transaction_bp.route('/<string:member_id>', methods=['POST','GET'])
def transaction(member_id=None):
    try:
        if request.method=="POST":            
         member_id=request.form.get('member')
        # cur=mysql.connection.cursor()
        # cur.execute("SELECT * FROM member")
        # data = cur.fetchall()
        # cur.close()
        print(member_id)
        data=transaction_model.get_transaction_member_list(member_id)
        member=member_model.getall()
        book=book_model.getbookwithauthor()
        # print(data)
        # print(member)
        
        return render_template('transaction.html',res={"trans_list":data,"member": member, "book": book,"member_id": member_id})
    except Exception as error:
        print(error)
        return render_template('error_occured.html')
    
@transaction_bp.route('/payment_entry', methods = ['POST'])
def payment_entry():
     if request.method=="POST":            
        member_id=request.form['member']
        amount=request.form['amount']
        comment=request.form['comment']
       
        error = validate(member_id,amount,comment)
        if error is None:
            try:        
                flash(transaction_model.insert_cr(member_id,amount,comment))
                data=transaction_model.get_transaction_member_list(member_id)
                member=member_model.getall()
                book=book_model.getbookwithauthor()       
                return render_template('transaction.html',res={"trans_list":data,"member": member, "book": book,"member_id": member_id})
            except Exception as error:
                print(error)
                return render_template('error_occured.html')
        else:
            flash(error)
            return redirect(url_for('issue_return_book_bp.issue_return_book'))

def validate(member_id,amount,comment):    
    error = None
    if not member_id:
        error = "member is required."
    elif not amount:
        error = "amount is required."  
    elif not comment:
        error = "comment is required."
    return error