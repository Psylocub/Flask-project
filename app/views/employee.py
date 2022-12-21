from flask import render_template, Blueprint, flash, request, redirect, url_for
from app.forms import AddEmployeeForm
from app.models import Employee, Company

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


@employee_blueprint.route("/staff/<string:company>", methods=["GET"])
def staff(company):
    company_selected = Company.query.filter_by(name=company).first()
    staff = company_selected.employees
    return render_template("employee/staff.html", company_name=company_selected, staff=staff)


@employee_blueprint.route("/delete-employee/<int:id>")
def delete_employee(id):
    employee_to_delete = Employee.query.filter_by(id=id).first()
    company = employee_to_delete.company
    employee_to_delete.delete_mix()
    return redirect(url_for("employee.staff", company=company))


@employee_blueprint.route("/update-employee/<int:id>")
def update_employee(id):
    employee_to_update = Employee.query.filter_by(id=id).first()
    form = AddEmployeeForm()
    if form.validate_on_submit():
        employee_to_update.name = form.name.data
        employee_to_update.position = form.position.data
        employee_to_update.phone = form.phone.data
        employee_to_update.email = form.email.data
        employee_to_update.birthday = form.birthday.data
        employee_to_update.save()
        flash("Employee successfully updated", "info")
        return redirect("employee.staff")
    elif form.is_submitted():
        flash("The given data was invalid.", "danger")
    elif request.method == "GET":
        form.name.data = employee_to_update.name
        form.position.data = employee_to_update.position
        form.phone.data = employee_to_update.phone
        form.email.data = employee_to_update.email
        form.birthday.data = employee_to_update.birthday
        form.company_id.data = Company.query.filter_by(id=employee_to_update.company_id).first()
    return render_template("employee/add_employee.html", id=id, form=form)