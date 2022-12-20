from flask import render_template, Blueprint, flash, request, redirect, url_for
from app.forms import AddEmployeeForm
from app.models import Employee

employee_blueprint = Blueprint("employee", __name__)

@employee_blueprint.route("/add-employee", methods=["GET", "POST"])
def add_employee():
    form = AddEmployeeForm()
    if form.validate_on_submit():
        employee = Employee(
            name=form.name.data,
            position=form.position.data,
            phone=form.phone.data,
            email=form.email.data,
            birthday=form.birthday.data,
            company_id=int(form.company_id.data.id),
        )
        employee.save()
        flash("Employee has been successfully added", "info")
        return redirect(url_for("main.index"))
    elif form.is_submitted():
        flash("The given data was invalid.", "danger")
    elif request.method == "GET":
        return render_template("employee/add_employee.html", form=form)
