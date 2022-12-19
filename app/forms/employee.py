from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms_sqlalchemy.fields import QuerySelectField
from app.models import Company


def choice_query():
    return Company.query

class AddEmployeeForm(FlaskForm):
    first_name = StringField("Employee name")
    position = StringField("Position")
    email = StringField("Email")
    company = QuerySelectField(query_factory=choice_query, allow_blank=True)
    submit = SubmitField("Save")