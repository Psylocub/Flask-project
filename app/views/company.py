from flask import render_template, Blueprint, flash, request, redirect, url_for
from app.forms import AddCompanyForm
from app.models import Company
from flask_login import login_required

company_blueprint = Blueprint("company", __name__)

@company_blueprint.route("/add-company", methods=["GET", "POST"])
@login_required
def add_company():
    form = AddCompanyForm()
    if form.validate_on_submit():
        company = Company(
            name=form.name.data,
            location=form.location.data,
        )
        company.save()
        flash("Company has been successfully added", "info")
        return redirect(url_for("main.index"))
    elif form.is_submitted():
        flash("The given data was invalid.", "danger")
    elif request.method == "GET":
        return render_template("company/add_company.html", form=form)

@company_blueprint.route("/delete-company/<int:id>")
@login_required
def delete_company(id):
    company_to_delete = Company.query.filter_by(id=id).first()
    company_to_delete.delete_mix()
    return redirect(url_for("main.index"))

@company_blueprint.route("/update-company/<int:id>", methods=["GET", "POST"])
@login_required
def update_company(id):
    company_to_update = Company.query.filter_by(id=id).first()
    form = AddCompanyForm()
    if form.validate_on_submit():
        company_to_update.name = form.name.data
        company_to_update.location = form.location.data
        company_to_update.save()
        flash("Company successfully updated", "info")
        return redirect(url_for("main.index"))
    elif form.is_submitted():
        flash("The given data was invalid.", "danger")
    elif request.method == "GET":
        form.name.data = company_to_update.name
        form.location.data = company_to_update.location
    return render_template("company/add_company.html", id=id, company=company_to_update, form=form)






















