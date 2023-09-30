from flask import Flask, render_template
from flask_login import LoginManager
import os
from application.database import *
from application.config import LocalDevelopmentConfig


login_manager = LoginManager()

@login_manager.user_loader
def load_user(id):
    return User.query.filter_by(id=id).first()

app=None
def create_app():
    app = Flask(__name__)
    if os.getenv('ENV', "development")== "production":
        raise Exception("Currently no production config is setup.")
    else:
        app.config.from_object(LocalDevelopmentConfig)
        
    db.init_app(app)
    app.app_context().push()
    login_manager.init_app(app)
    app.app_context().push()
    db.create_all()
    return app
app=create_app()

@app.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return render_template('404.html'), 404

# importing all the controllers here
from application.category_view import *
from application.product_view import *
from application.user_view import *
from application.order_view import *

if __name__=='__main__':
    app.run(debug=True)
