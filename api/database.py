from sqlalchemy import ForeignKey, Integer, String, Boolean, Date
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship

from flask_sqlalchemy import SQLAlchemy
from datetime import date


class Base(DeclarativeBase):
    pass


db = SQLAlchemy(model_class=Base)


# Constants for roles
ADMIN_ROLE = "Admin"
USER_ROLE = "User"


# Role Model
class Role(db.Model):
    __tablename__ = "role"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)

    def __repr__(self):
        return f"<Role {self.name}>"


class User(db.Model):

    __tablename__ = "user"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    email: Mapped[str] = mapped_column(String(100), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(String(100), unique=True, nullable=False)

    # is_sso field with default value False
    is_sso: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)

    # Relationship
    profile: Mapped["Profile"] = relationship(back_populates="user", uselist=False)

    # Relationship with Role model
    role: Mapped["Role"] = relationship("Role", backref="users")

    def __repr__(self):
        return f"<User {self.email}, Role: {self.role.name}>"


class Profile(db.Model):

    __tablename__ = "profile"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"), nullable=False)

    first_name: Mapped[str] = mapped_column(String(100))
    last_name: Mapped[str] = mapped_column(String(100))
    date_of_birth: Mapped[date] = mapped_column(Date)
    bio: Mapped[str] = mapped_column(String(250))

    # Relationship
    user: Mapped[User] = relationship(back_populates="profile")

    def __repr__(self):
        return f"<Profile {self.first_name} {self.last_name}>"
