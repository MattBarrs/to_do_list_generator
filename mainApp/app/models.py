from app import db

class taskToDo(db.Model):
    Id = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String(50), index=True, unique=False, nullable=False)
    Details = db.Column(db.String(500), index=True, unique=False, nullable=False)
    Completed = db.Column(db.Boolean, default=False, nullable=True)
