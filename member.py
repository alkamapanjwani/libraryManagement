from app import mysql
import app

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
    try:
        if request.method=="POST":            
            name=request.form['name']
            email=request.form['email']
            phone=request.form['phone']
            flash(member_model.insert(name,email,phone))
            return redirect(url_for('member_bp.member'))
    except Exception as error:
        return render_template('error_occured.html')

@member_bp.route('/update_member',methods=['POST','GET'])
def update_member():
    try:
        if request.method == 'POST':
            id_data = request.form['id']
            name = request.form['name']
            email = request.form['email']
            phone = request.form['phone']
            flash(member_model.update(name,email,phone,id_data)) 
            return redirect(url_for('member_bp.member'))
    except Exception as error:
        return render_template('error_occured.html')

@member_bp.route('/delete_member/<string:id_data>', methods = ['GET'])
def delete_member(id_data):
    try:
        flash(member_model.delete(id_data)) 
        return redirect(url_for('member_bp.member'))
    except Exception as error:
        return render_template('error_occured.html')
