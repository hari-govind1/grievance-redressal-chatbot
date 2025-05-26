from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

# Initialize the database
db = SQLAlchemy()

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)
    department = db.Column(db.String(150), nullable=False)  # Store department name
