from app import app, db
from app.models import User, Post
import logging
from logging.handlers import SMTPHandler

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Post': Post}

