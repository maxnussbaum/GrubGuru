from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField
from wtforms.validators import DataRequired, required

class SearchForm(FlaskForm):
    search = StringField('search', validators=[required(), DataRequired()])
