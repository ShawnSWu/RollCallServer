from app.database import db


class ToDoEntity(db.Model):
    __tablename__ = 'todo_note'
    account = db.Column(db.String(255), primary_key=True)
    todo_title = db.Column(db.String(255), nullable=True)
    todo_createtime = db.Column(db.String(15), nullable=True)
    todo_isFinsh = db.Column(db.Integer, nullable=True)
