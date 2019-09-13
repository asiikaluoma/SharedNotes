from app import db

class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(),
    onupdate=db.func.current_timestamp())

    title = db.Column(db.String(144), nullable=False)
    body = db.Column(db.String(1000), nullable=False)

    def __init__(self, title, body):
        self.title = title
        self.body = body
        self.done = False