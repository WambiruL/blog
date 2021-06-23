from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField,SubmitField
from wtforms.validators import Required

class PostForm(FlaskForm):
    title = StringField("Blog title:", validators=[Required()])
    post = TextAreaField("Write a blog:", validators=[Required()])
    submit = SubmitField("Post")

class CommentForm(FlaskForm):
    comment = TextAreaField("Post Comment", validators=[Required()])
    alias = StringField("Comment Alias")
    submit = SubmitField("Comment")


class UpdatePostForm(FlaskForm):
    title = StringField("Blog title", validators=[Required()])
    post = TextAreaField("Wtite a blog", validators=[Required()])
    submit = SubmitField("Update")
