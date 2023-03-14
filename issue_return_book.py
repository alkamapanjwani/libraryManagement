from app import mysql
import app
import re
import urllib.request, json
from flask import Blueprint, render_template, request, redirect, url_for, flash
from models.issue_return_book_model import issue_return_book_model
from models.book_model import book_model
from models.member_model import member_model
from models.setting_model import Setting_model
from models.transaction_model import transaction_model
from models.book_stock_model import book_stock_model

issue_return_book_model = issue_return_book_model()
book_model = book_model()
member_model = member_model()
setting_model = Setting_model()
transaction_model = transaction_model()
book_stock_model = book_stock_model()

issue_return_book_bp = Blueprint(
    "issue_return_book_bp", __name__, url_prefix="/issue_return_book"
)


@issue_return_book_bp.route("/")
def issue_return_book():
    try:
        # cur=mysql.connection.cursor()
        # cur.execute("SELECT * FROM member")
        # data = cur.fetchall()
        # cur.close()

        data = issue_return_book_model.get_issue_return_book_list()
        member = member_model.getall()
        book = book_model.getbookwithauthor()
        # print(data)
        return render_template(
            "issue_return_book.html",
            res={"issue_list": data, "member": member, "book": book},
        )
    except Exception as error:
        print(error)
        return render_template("error_occured.html")


@issue_return_book_bp.route("/issue_book", methods=["POST"])
def issue_book():
    if request.method == "POST":
        member_id = request.form["member"]
        book_id = request.form["book"]

        error = validate(member_id, book_id)
        if error is None:
            try:
                flash(issue_return_book_model.mark_issue(member_id, book_id))
                return redirect(url_for("issue_return_book_bp.issue_return_book"))
            except Exception as error:
                print(error)
                return render_template("error_occured.html")
        else:
            flash(error)
            return redirect(url_for("issue_return_book_bp.issue_return_book"))


@issue_return_book_bp.route("/return_book/<string:id_data>", methods=["GET"])
def return_book(id_data):
    try:
        flash(issue_return_book_model.mark_return(id_data))
        return redirect(url_for("issue_return_book_bp.issue_return_book"))
    except Exception as error:
        print(error)
        return render_template("error_occured.html")


def validate(member_id, book_id):
    error = None
    if not member_id:
        error = "member is required."
    elif not book_id:
        error = "book is required."
    elif (
        transaction_model.get_amount_payable_member(member_id)
        >= setting_model.get_outstanding_debt()
    ):
        error = "please clear outstanding debt first before new issue"
    elif not (book_stock_model.get_available_book_qty(book_id) > 0):
        error = "book not in stock"

    return error
