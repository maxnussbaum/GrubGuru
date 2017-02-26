from flask_wtf import Form
from wtforms import StringField, BooleanField
from wtforms.validators import DataRequired, required

class SearchForm(Form):
    search = StringField('search', validators=[required(), DataRequired()])
