from app import db
from app.models import Base

from sqlalchemy.sql import text

class UserNotebook(db.Model):
    __tablename__ = 'usernotebook'

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
    
    @staticmethod
    def user_notebook_note_counts(id):
        stmt = text("SELECT un.notebook_id, n.title, count(distinct no.id), count(distinct c.account_id)"
        " FROM usernotebook un"
        " LEFT JOIN Notebook n ON n.id=un.notebook_id"
        " LEFT JOIN usernotebook c ON c.notebook_id=n.id"
        " LEFT JOIN Note no ON no.notebook_id=n.id"
        " WHERE un.account_id=:id"
        " GROUP BY un.notebook_id, n.title").params(id=id)
        res = db.engine.execute(stmt)
  
        response = []
        for row in res:
            response.append({"id":row[0], "title": row[1], "count":row[2], "users":row[3]})
        
        return response