from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column
from src.infrastructure import db

class Contact(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str]
    phone_number: Mapped[str]