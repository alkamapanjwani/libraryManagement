from app import mysql
import app
import re
from flask import Blueprint, render_template, request, redirect, url_for, flash
from models.author_model import author_model

author_model = author_model()

author_bp = Blueprint("author_bp", __name__, url_prefix="/author")


@author_bp.route("/")
def author():
    try:
        data = author_model.getall()
        return render_template("author.html", author=data)
    except Exception as error:
        print(error)
        return render_template("error_occured.html")


@author_bp.route("/insert_author", methods=["POST"])
def insert_author():
    if request.method == "POST":
        name = request.form["name"]

        error = validate(name)
        if error is None:
            try:
                flash(author_model.insert(name))
                return redirect(url_for("author_bp.author"))
            except Exception as error:
                print(error)
                print(name)
                return render_template("error_occured.html")
        else:
            flash(error)
            return redirect(url_for("author_bp.author"))


@author_bp.route("/update_author", methods=["POST", "GET"])
def update_author():
    if request.method == "POST":
        id_data = request.form["id"]
        name = request.form["name"]

        error = validate(name)
        if error is None:
            try:
                flash(author_model.update(name, id_data))
                return redirect(url_for("author_bp.author"))
            except Exception as error:
                print(error)
                return render_template("error_occured.html")
        else:
            flash(error)
            return redirect(url_for("author_bp.author"))


@author_bp.route("/delete_author/<string:id_data>", methods=["GET"])
def delete_author(id_data):
    try:
        flash(author_model.delete(id_data))
        return redirect(url_for("author_bp.author"))
    except Exception as error:
        return render_template("error_occured.html")


def validate(name):
    error = None
    if not name:
        error = "name is required."
    return error
