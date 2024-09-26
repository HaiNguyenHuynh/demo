import os


class Config:
    """Base configuration settings."""

    # General Flask settings
    SECRET_KEY = os.getenv("SECRET_KEY", "averylongsecretkey")

    # Database settings
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "sqlite:///project.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = (
        False  # Turn off modification tracking for performance
    )


class DevelopmentConfig(Config):
    """Development-specific settings."""

    DEBUG = True


class ProductionConfig(Config):
    """Production-specific settings."""

    DEBUG = False
    SQLALCHEMY_DATABASE_URI = os.getenv(
        "DATABASE_URL", "postgresql://user:password@localhost/dbname"
    )  # Replace with production DB


# You can add other configuration classes (e.g., TestingConfig) as needed.
