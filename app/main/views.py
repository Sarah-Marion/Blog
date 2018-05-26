from flask import render_template, redirect, url_for, flash
from flask_login import login_required, current_user
from flask_admin.contrib.sqla import ModelView
from . forms import PostForm, CommentForm, SubscribersForm
from .import main
from .. import db, basic_auth
import markdown2
from .email import mail_message
from ..models import User, Post, Role, Comment, Subscribers
from datetime import datetime

@main.route('/',methods=['POST','GET'])
def index():
    title= "Blog On | Home "
    all = Post.query.all()
    all.reverse()
  
    subscribers = SubscribersForm()
    try:
        if subscribers.validate_on_submit():
            subscriber = Subscribers(email = subscribers.email.data)
            db.session.add(subscriber)
            db.session.commit()
            flash('You are now subscribed!')
            mail_message("Welcome to Blog On","email/welcome",subscriber.email,subscriber=subscriber)
            print("sent")
            return redirect(url_for('main.index'))
    except:
        return redirect(url_for('main.index'))
        
        
    return render_template('index.html', title = title, posts=all, subscribers=subscribers)
    