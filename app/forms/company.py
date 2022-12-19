from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length


class AddCompanyForm(FlaskForm):
    name = StringField("Company name", [DataRequired(), Length(1, 50)])
    location = StringField("Location", [DataRequired(), Length(5, 50)])
    submit = SubmitField("Save")


