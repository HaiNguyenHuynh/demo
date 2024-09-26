from sqlalchemy import ForeignKey, Integer, String, Boolean, Date, event
from sqlalchemy.orm import (
    DeclarativeBase,
    Mapped,
    mapped_column,
    relationship,
    sessionmaker,
)

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

    # Relationship to User model
    users = relationship("User", back_populates="role")

    def __repr__(self):
        return f"<Role {self.name}>"


class User(db.Model):

    __tablename__ = "user"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    email: Mapped[str] = mapped_column(String(100), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(
        String(100), nullable=True
    )  # Password can be nullable for SSO users

    # is_sso field with default value False
    is_sso: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)

    # Foreign key linking to Role
    role_id: Mapped[int] = mapped_column(ForeignKey("role.id"), nullable=False)

    # Relationship with Role model
    role: Mapped["Role"] = relationship("Role", back_populates="users")

    # Relationship with Profile model
    profile: Mapped["Profile"] = relationship(back_populates="user", uselist=False)

    def __repr__(self):
        return f"<User {self.email}, Role: {self.role.name}>"


class Profile(db.Model):

    __tablename__ = "profile"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"), nullable=False)

    first_name: Mapped[str] = mapped_column(String(100), nullable=True)
    last_name: Mapped[str] = mapped_column(String(100), nullable=True)
    date_of_birth: Mapped[date] = mapped_column(Date, nullable=True)
    bio: Mapped[str] = mapped_column(String(250), nullable=True)

    # Relationship
    user: Mapped[User] = relationship(back_populates="profile")

    def __repr__(self):
        return f"<Profile {self.first_name} {self.last_name}>"


# -------- Event listener to auto-create Profile after User creation --------


@event.listens_for(User, "after_insert")
def create_empty_profile(mapper, connection, target):
    """
    Automatically create an empty Profile for a new User after they are inserted into the database.
    """
    # Create a session for this operation
    session = sessionmaker(bind=connection)()

    # Create a new profile with empty values
    new_profile = Profile(first_name="", last_name="", bio="", user_id=target.id)

    # Add and commit the new profile
    session.add(new_profile)
    session.commit()


# Auto-assign default role after a User is inserted
@event.listens_for(User, "before_insert")
def assign_default_role(mapper, connection, target):
    """
    Automatically assign the 'User' role if no role is specified for the new User.
    """
    session = sessionmaker(bind=connection)()

    # Assign default role if the user doesn't have a role
    if not target.role:
        default_role = session.query(Role).filter_by(name="User").first()
        if default_role:
            target.role = default_role
        else:
            raise ValueError("Default role 'User' does not exist in the database.")
