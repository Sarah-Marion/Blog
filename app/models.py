from flask_login import UserMixin, current_user, login_manager
from werkzeug.security import generate_password_hash, check_password_hash
from . import login_manager
from datetime import datetime
from . import db, admin
from flask_admin.contrib.sqla import ModelView

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(UserMixin,db.Model):
    """ 
    class modelling the users by handling the login
    """

    __tablename__ = 'users'

    #create the columns
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    username = db.Column(db.String, unique=True, index=True)
    email = db.Column(db.String, unique=True, index=True)
    pass_secure = db.Column(db.String)


    # securing passwords
    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')
    @password.setter
    def password(self, password):
        self.pass_secure = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.pass_secure, password)

    posts = db.relationship('Post', backref='author', lazy='dynamic')
    is_admin = db.Column(db.Boolean)
    comment_id = db.Column(db.Integer, db.ForeignKey('comments.id'))
    

    def __repr__(self):
        return f'User{self.username}'
