from flask import Flask
from sqlalchemy import ForeignKey, Integer, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship

from flask_sqlalchemy import SQLAlchemy

class Base(DeclarativeBase):
  pass

db = SQLAlchemy(model_class=Base)


class User(db.Model):

    __tablename__ = "user"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    email: Mapped[str] = mapped_column(String(100), unique=True, nullable=False)

    # Relationship
    profile: Mapped["Profile"] = relationship(back_populates="user", uselist=False)


class Profile(db.Model):

    __tablename__ = "profile"

    id: Mapped[int] =  mapped_column(Integer, primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey('user.id'), nullable=False)
    bio: Mapped[str] = mapped_column(String(250))

    # Relationship
    user: Mapped[User] = relationship(back_populates="profile")
