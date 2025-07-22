from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length

class CompletionReq(FlaskForm):
    """基础聊天请求验证"""
    # 必填
    query = StringField("query", validators=[
        DataRequired(message="query不能为空"),
        Length(max=1000, message="query长度不能超过1000字符")
    ])