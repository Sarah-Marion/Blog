{% extends 'base.html' %}
{% import 'bootstrap/wtf.html' as wtf %}

{% block content %}
<div class="header">
    <div class="intro">
        <h1 class="display-4">Hey There {{current_user.username}}!..</h1>
        {% if current_user.is_admin %}
        <p>Welcome to Blog On!... You can now start posting your articles here!...</p> 
        <button><a href="{{url_for('main.post')}}">Post article</a> </button> 
        {% else %}
        <p>Welcome! You can now Read and share articles!..</p>
        <div class="subscribers">
        {{wtf.quick_form(subscribers)}}
        {% for message in get_flashed_messages() %}
            <div class="alert alert-danger">
            <button type="button" class="close" data-dismiss="alert">&times;</button>
            {{ message }}
            </div>
        {% endfor %}
        </div>
        {% endif %}
    </div>
</div>

<div class="container-fluid">
    <div class="row posts">
        {% for post in posts %}
        <div class="col-md-5 article">
            <div class="wrap">
                <h4>
                    <a href="{{url_for('main.fullpost',id=post.id)}}">{{post.title}}</a>
                </h4>
                <hr>
                <br>
                <i><sub>{{post.timeposted}}</sub></i>
                <br>
                {{post.post | truncate(250)}}
                <br>
            <button>
                <a href="{{url_for('main.fullpost',id=post.id)}}">Read article</a>
            </button>
            </div> 
        </div>
        {% endfor %}
    </div>
</div>
{% endblock %}