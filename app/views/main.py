from flask import render_template, Blueprint
from app.models import Company, Employee


main_blueprint = Blueprint("main", __name__)

@main_blueprint.route("/")
def index():
    companies = Company.query.order_by(Company.name.asc()).all()
    employees = Employee.query.all()
    return render_template("index.html", companies=companies, employees=employees)
