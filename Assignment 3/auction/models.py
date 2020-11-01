from datetime import datetime
from . import db
from flask_login import UserMixin


class User(db.Model, UserMixin):
    __tablename__= 'users'
    id = db.Column(db.Integer, primary_key=True)
    fullname = db.Column(db.String(80), nullable=False)
    phonenumber = db.Column(db.Integer)
    address = db.Column(db.String(80), nullable=False)
    name = db.Column(db.String(100), index=True, unique=True, nullable=False)
    emailid = db.Column(db.String(100), index=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)

    def __repr__(self): 
        return "<Name: {}>".format(self.user)

class Book(db.Model):
    __tablename__ = 'books'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    category = db.Column(db.String(200), nullable=False)
    description = db.Column(db.String(200), nullable=False)
    image = db.Column(db.String(400), nullable=False)
    price = db.Column(db.Integer, db.ForeignKey('books.id'))
    bids = db.relationship('Bid', backref ='user')  
    
  

    def __repr__(self): 
        return "<Name: {}>".format(self.name)


class Bid(db.Model):
    __tablename__ = 'bids'
    id = db.Column(db.Integer, primary_key=True)
    bid = db.Column(db.Integer, db.ForeignKey('bids.id'))
    created_at = db.Column(db.DateTime, default=datetime.now())
    
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    book_id = db.Column(db.Integer, db.ForeignKey('books.id'))
    
    def __repr__(self):
        return "<Bid: {}>".format(self.bid)

class Watchlist(db.Model):
    __tablename__ = 'watchlist'
    id = db.Column(db.Integer, primary_key=True)
    date_added = db.Column(db.DateTime, default=datetime.now())
    book_id = db.Column(db.Integer, db.ForeignKey('books.id'))
    bid = db.Column(db.Integer, db.ForeignKey('bids.id'))





