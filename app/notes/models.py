from app import db
from app.models import Base

class Note(Base):
    
    title = db.Column(db.String(144), nullable=False)
    body = db.Column(db.String(1000), nullable=False)

    notebook_id = db.Column(db.Integer, db.ForeignKey('notebook.id'), nullable=False)
    creator_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=False)

    def __init__(self, title, body):
        self.title = title
        self.body = body