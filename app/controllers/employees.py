import csv
import tempfile
from datetime import date, datetime
from typing import Optional
from werkzeug.datastructures import FileStorage
from app import db

from pydantic import BaseModel, validator

from app.models import Employee, Company


class EmployeeRow(BaseModel):
    name: Optional[str]
    position: Optional[str]
    phone: Optional[str]
    email: Optional[str]
    birthday: Optional[date]

    @validator("birthday", pre=True,)
    def parse_birthday(cls, value: str) -> date:
        return datetime.strptime(value, "%d.%m.%Y").date()


def upload_employee_controller(input_file: FileStorage):
    with tempfile.NamedTemporaryFile(delete=True) as temp_file:
        file_path = temp_file.name
        with open(file_path, "wb") as examined_file:
            begin_data = input_file.read(3)
            if b"\xef\xbb\xbf" not in begin_data:
                examined_file.write(begin_data)
            examined_file.write(input_file.read())
        with open(file_path, mode="r") as read_file:
            reader = csv.DictReader(read_file)
            reader.fieldnames = [
                name.lower().replace(" ", "_") for name in reader.fieldnames
            ]
            for row in reader:
                r: EmployeeRow = EmployeeRow.parse_obj(row)
                r_exist = (
                    db.session.query(Employee)
                    .filter_by(
                        name=r.name,
                        position=r.position,
                        phone=r.phone,
                        email=r.email,
                        birthday=r.birthday,
                    )
                    .first()
                )
                if r_exist:
                    pass
                else:
                    employee = Employee(**r.dict())
                    employee.save()
            db.session.commit()
