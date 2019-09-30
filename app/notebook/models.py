from app import db
from app.models import Base

from sqlalchemy.sql import text

class Notebook(Base):
    
    title = db.Column(db.String(255), nullable=False)
    description = db.Column(db.String(1000), nullable=True)

    owner_id = db.Column(db.Integer, db.ForeignKey('account.id'),
                           nullable=False)
    users = db.relationship("UserNotebook", back_populates="child")
    notes = db.relationship("Note", backref='note', lazy=True)

    def __init__(self, title, description):
        self.title = title
        self.description = description

    @staticmethod
    def find_note_count():
        stmt = text("SELECT COUNT(*) FROM Notebook"
                    " INNER JOIN Note ON Notebook.id = Note.notebook_id")
        res = db.engine.execute(stmt)
  
        for row in res:
            return row[0]