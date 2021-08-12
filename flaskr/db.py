from flask_sqlalchemy import SQLAlchemy

import click
from flask import current_app
from flask.cli import with_appcontext

db = SQLAlchemy()


def get_db():
    return db


def close_db(e=None):
    if db is not None:
        db.session.close()


def init_db():
    db.init_app(current_app)
    db.create_all()

@click.command('init-db')
@with_appcontext
def init_db_command():
    """Clear the existing data and create new tables."""
    init_db()
    click.echo('Initialized the database.')