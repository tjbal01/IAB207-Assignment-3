from flask import Blueprint, render_template, request, session, redirect, url_for
from .models import Book

mainbp = Blueprint ('main' ,__name__)

@mainbp.route('/')
def index():
    books = Book.query.all()
    return render_template('index.html', books=books)

@mainbp.route('/search')
def search():
    if request.args['search']:
        dest = "%" + request.args['search'] + '%'
        books = Book.query.filter(Book.category.like(dest)).all()
        return render_template('index.html', books=books)
    else:
        return redirect(url_for('main.index'))



