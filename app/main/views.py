from flask import render_template
from ..models import Post
from . import main

@main.route("/", methods = ["GET", "POST"])
def index():
    posts = Post.get_all_posts()
   

    return render_template("index.html", posts = posts)
                        