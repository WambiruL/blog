from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField,SubmitField
from wtforms.validators import Required

class PostForm(FlaskForm):
    title = StringField("Blog title:", validators=[Required()])
    post = TextAreaField("Type Away:", validators=[Required()])
    submit = SubmitField("Post")

class CommentForm(FlaskForm):
    comment = TextAreaField("Post Comment", validators=[Required()])
    alias = StringField("Comment Alias")
    submit = SubmitField("Comment")
