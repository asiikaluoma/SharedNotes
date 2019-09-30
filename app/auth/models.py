from app import db
from app.models import Base

class UserNotebook(db.Model):
    __tablename__ = 'UserNotebook'
    account_id = db.Column(db.Integer, db.ForeignKey('account.id'), primary_key=True)
    notebook_id = db.Column(db.Integer, db.ForeignKey('notebook.id'), primary_key=True)
    #extra_data = Column(String(50))
    child = db.relationship("Notebook", back_populates="users")
    parent = db.relationship("User", back_populates="notebooks")


class User(Base):
    __tablename__ = "account"
    
    name = db.Column(db.String(144), nullable=False)
    username = db.Column(db.String(144), nullable=False)
    password = db.Column(db.String(144), nullable=False)
    notebooks = db.relationship("UserNotebook", back_populates="parent")

    def __init__(self, name, username, password):
        self.name = name
        self.username = username
        self.password = password
  
    def get_id(self):
        return self.id

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def is_authenticated(self):
        return True