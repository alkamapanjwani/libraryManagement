from app import mysql
import app
import re
from flask import Blueprint,render_template, request, redirect, url_for, flash
from models.member_model import member_model

member_model = member_model()

member_bp = Blueprint('member_bp', __name__, url_prefix="/member")

@member_bp.route('/')
def member():
    try:
        # cur=mysql.connection.cursor()
        # cur.execute("SELECT * FROM member")
        # data = cur.fetchall()
        # cur.close()
        data=member_model.getall()
        return render_template('member.html',member=data)
    except Exception as error:
        print(error)
        return render_template('error_occured.html')

@member_bp.route('/insert_member', methods=['POST'])
def insert_member():
    if request.method=="POST":            
        name=request.form['name']
        email=request.form['email']
        phone=request.form['phone']
        error = validate(name,email,phone)
        if error is None:
            try:        
                flash(member_model.insert(name,email,phone))
                return redirect(url_for('member_bp.member'))
            except Exception as error:
                print(error)
                return render_template('error_occured.html')
        else:
            flash(error)
            return redirect(url_for('member_bp.member'))


@member_bp.route('/update_member',methods=['POST','GET'])
def update_member():
    if request.method=="POST":
        id_data = request.form['id']            
        name=request.form['name']
        email=request.form['email']
        phone=request.form['phone']
        error = validate(name,email,phone)
        if error is None:
            try:        
                flash(member_model.update(name,email,phone,id_data)) 
                return redirect(url_for('member_bp.member'))
            except Exception as error:
                print(error)
                return render_template('error_occured.html')
        else:
            flash(error)
            return redirect(url_for('member_bp.member'))



@member_bp.route('/delete_member/<string:id_data>', methods = ['GET'])
def delete_member(id_data):
    try:
        flash(member_model.delete(id_data)) 
        return redirect(url_for('member_bp.member'))
    except Exception as error:
        return render_template('error_occured.html')
    
regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'

def validate(name,email,phone):    
    error = None
    if not name:
        error = "name is required."
    elif not email:
        error = "email is required."
    elif not re.fullmatch(regex, email):
        error = "email is not valid."
    elif not phone:
        error = "phone is required."
    return error