from flask import Flask, render_template 
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

db=SQLAlchemy()




def create_app():
    app=Flask(__name__) 
    app.debug=True
    app.secret_key='utroutoru'
   
    #set the app configuration data 
    
    app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///auction123.sqlite'
   
    #initialize db with flask app
    
    db.init_app(app)

    UPLOAD_FOLDER = '/static/image'
    app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

    login_manager = LoginManager()
    login_manager.login_view='authentication.login'
    login_manager.init_app(app)

    from .models import User 
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    @app.errorhandler(404) 
    def not_found(e): 
        return render_template("404.html") 

    
    bootstrap = Bootstrap(app)

    from . import views
    app.register_blueprint(views.mainbp)

    from . import books
    app.register_blueprint(books.bp)

    from . import authentication
    app.register_blueprint(authentication.bp)

    return app

