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

@main.route('/',methods=['GET', 'POST'])
def index():
    title= "Blog On | Home "
    all = Post.query.order_by('-id').all()
    print(f'blogs {all}')
  
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
    


@main.route('/profile/<username>')
@login_required

def profile(username):
    
    user = User.query.filter_by(username = username).first_or_404()
    title = "Profile"       
    return render_template('profile.html' , user=user,title=title)

@main.route('/post', methods=['GET', 'POST'])
def post():
    all = Post.query.all()
    all.reverse()
    print(all)

    Comments = CommentForm()
    if Comments.validate_on_submit():
        comment = Comment(comment = Comments.comment.data, commenter = Comments.commenter.data)
        db.session.add(comment)
        db.session.commit()
        print(comment)
        return redirect(url_for('main.post'))

    allcomments = Comment.query.all()
    title = "Post Article"
    Blog = PostForm()
    # try:
    if Blog.validate_on_submit():
        post = Post( title = Blog.title.data ,post = Blog.Entry.data, user_id = current_user.id, timeposted = datetime.utcnow() )
        db.session.add(post)
        db.session.commit()
        return redirect(url_for('main.post'))
    # except:
    #     flash("Sorry you can NOT post more than 225 characters for now. We are aware of this situation and are currently working on this.")
    #     return redirect(url_for('main.post'))

    return render_template('post.html', Post = Blog, title = title, posts = all, comment = Comments, allcomments = allcomments)



@main.route('/post/<id>', methods=['POST','GET'])
def fullpost(id):
    
    title= f'Posts' 
    post = Post.query.filter_by(id=id).first()
    Comments = CommentForm()
    if Comments.validate_on_submit():
        comment = Comment(comment = Comments.comment.data, post_id=id, commenter = Comments.commenter.data)
        db.session.add(comment)
        db.session.commit()
        print(comment)
        return redirect(url_for('main.fullpost', id=post.id))
    allcomments = Comment.query.all()
    postcomments = Comment.query.filter_by(post_id=id).all()
     

    return render_template('fullpost.html', title = title, post = post, comment = Comments, allcomments = allcomments, postcomments = postcomments)

            

@main.route('/<int:id>/delete', methods=['POST'])
@login_required
def delete(id):
    get_post(id)
    db = get_db()
    db.execute('DELETE FROM post WHERE id = ?, (id,)')
    db.commit()
    return redirect(url_for('main.index'))