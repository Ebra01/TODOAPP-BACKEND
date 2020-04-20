from flask_sqlalchemy import SQLAlchemy
import os


db = SQLAlchemy()


def setup_db(app):
    # Setting up Database

    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.app = app
    db.init_app(app)
    db.create_all()

# MODELS : TABLES


class Todo(db.Model):
    """
    Todos Table including insert, update, and delete functions
    to make CRID prosess easier.
    """
    __tablename__ = 'todos'

    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String, nullable=False)
    finished = db.Column(db.Boolean, nullable=False, default=False)

    def __init__(self, content, finished):
        self.content = content
        self.finished = finished

    def display(self):
        return {
            'id': self.id,
            'content': self.content,
            'finished': self.finished
        }

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def update(self):
        db.session.commit()
