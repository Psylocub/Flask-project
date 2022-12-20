from app import db
from app.models.utils import ModelMixin


class Company(db.Model, ModelMixin):
    __tablename__="company"

    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(50), nullable=False)
    location = db.Column(db.String(50), nullable=False)
    employees = db.relationship("Employee", back_populates="company")

    def __repr__(self):
        return self.name
