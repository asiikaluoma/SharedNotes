from app import db

class UserNotebook(db.Model):
    __tablename__ = 'UserNotebook'
    account_id = db.Column(db.Integer, db.ForeignKey('account.id'), primary_key=True)
    notebook_id = db.Column(db.Integer, db.ForeignKey('notebook.id'), primary_key=True)
    #extra_data = Column(String(50))
    child = db.relationship("Notebook", back_populates="users")
    parent = db.relationship("User", back_populates="notebooks")


class User(db.Model):

    __tablename__ = "account"
  
    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(),
                              onupdate=db.func.current_timestamp())

    name = db.Column(db.String(144), nullable=False)
    username = db.Column(db.String(144), nullable=False)
    password = db.Column(db.String(144), nullable=False)

    #notebooks = db.relationship("Notebook", backref='account', lazy=True)
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