from flask import (Blueprint, render_template, request, url_for, redirect) 
from .models import Book, Bid, User
from .forms import BidForm, BookForm
from . import db
from flask_login import login_required, current_user
import os
from werkzeug.utils import secure_filename




bp = Blueprint('book', __name__, url_prefix='/books')


@bp.route('/<id>') 
def show(id): 
  book = Book.query.filter_by(id=id).first()  
  bidForm = BidForm()
  return render_template('books/show.html', book=book, form=bidForm)

 


@bp.route('/<id>/bid', methods=['GET', 'POST'])  
@login_required
def bid(id):  
  bidForm = BidForm()
  book_obj = Book.query.filter_by(id=id).first()
  if bidForm.validate_on_submit():
    bid = Bid(bid=bidForm.bid.data, book=book_obj, user = current_user) 
    db.session.add(bid) 
    db.session.commit() 
      
  return redirect(url_for('book.show', id=id))






def check_upload_file(form):
  fp = form.image.data
  filename=fp.filename
  BASE_PATH=os.path.dirname(__file__)

  upload_path = os.path.join(BASE_PATH, 'static/image', secure_filename(filename))
  db_upload_path = '/static/image/'+ secure_filename(filename)
  fp.save(upload_path)
  return db_upload_path






@bp.route('/create', methods = ['GET', 'POST'])
@login_required
def create():
  form = BookForm()
  if form.validate_on_submit():
    db_file_path = check_upload_file(form)
    # if the form was successfully submitted
    # access the values in the form data
    book = Book(name=form.name.data, category=form.category.data,
                description=form.description.data,
                image=db_file_path,
                price=form.price.data)
    # add the object to the db session
    db.session.add(book)
    # commit to the database
    db.session.commit()

    
    print('Successfully created new listing', 'success')
    return redirect(url_for('book.create'))

  return render_template('books/create.html', form=form)




 




