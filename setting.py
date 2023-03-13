from app import mysql
import app
import re
from flask import Blueprint,render_template, request, redirect, url_for, flash
from models.setting_model import Setting_model

setting_model = Setting_model()

setting_bp = Blueprint('setting_bp', __name__, url_prefix="/setting")

@setting_bp.route('/', methods=['POST','GET'])
def setting():
    if request.method=="POST":       
        outstanding_debt=request.form['outstanding_debt']
        book_fees=request.form['book_fees']

        error = validate(outstanding_debt,book_fees)
        if error is None:
            try:        
                flash(setting_model.update(outstanding_debt,book_fees)) 
                return redirect(url_for('setting_bp.setting'))
            except Exception as error:
                print(error)
                return render_template('error_occured.html')
        else:
            flash(error)
            return redirect(url_for('setting_bp.setting'))
    else:
        data=setting_model.get_outstanding_debt()
        book_fees=setting_model.get_book_fees()
        return render_template('setting.html', res={"outstanding_debt":data,"book_fees":book_fees})

def validate(outstanding_debt,book_fees):    
    error = None
    if not outstanding_debt:
        error = "outstanding_debt is required."  
    if not book_fees:
        error = "book_fees is required."  
    return error