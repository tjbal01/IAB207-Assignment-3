from flask_wtf import FlaskForm
from wtforms.fields import TextAreaField,SubmitField, StringField, PasswordField
from wtforms.validators import InputRequired, Length, Email, EqualTo
from flask_wtf.file import FileRequired, FileField, FileAllowed

ALLOWED_FILE = {'png', 'jpg', 'JPG', 'PNG'}



class BookForm(FlaskForm):
  name = StringField('Title', validators=[InputRequired()])
  
  description = TextAreaField('Description', validators=[InputRequired()])
  
  category = StringField('Category', validators =[InputRequired()])
 
  image = FileField('Book Image', validators=[FileRequired(message='Image can not be empty'),
                                         FileAllowed(ALLOWED_FILE, message='Only support png, jpg, JPG, PNG, bmp')])
   
  price = StringField('Starting price', validators=[InputRequired()])

  submit = SubmitField("Create")

  

  
class BidForm(FlaskForm):
  bid = StringField('Bid', [InputRequired()])
  submit = SubmitField('Add bid')

  




class LoginForm(FlaskForm):
    user_name=StringField("User Name", validators=[InputRequired('Enter user name')])
    password=PasswordField("Password", validators=[InputRequired('Enter user password')])
    submit = SubmitField("Login")

 
class RegisterForm(FlaskForm):
    fullname = StringField('Full Name', validators=[InputRequired()])
    phonenumber = StringField('Phone Number', validators=[InputRequired()])
    address = StringField('Adress', validators=[InputRequired()])
    user_name=StringField("User Name", validators=[InputRequired()])
    email_id = StringField("Email Address", validators=[Email("Please enter a valid email")])
    
    
    password=PasswordField("Password", validators=[InputRequired(),
                  EqualTo('confirm', message="Passwords should match")])
    confirm = PasswordField("Confirm Password")
    
    submit = SubmitField("Register")


   