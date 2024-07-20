import json

import click
from flask import current_app
from flask.cli import FlaskGroup, run_command, with_appcontext

from ragbackend import settings
from ragbackend.app import create_app



def create():
    app = current_app or create_app()

    @app.shell_context_processor
    def shell_context():
        from ragbackend import settings

        return {"settings": settings}

    return app


@click.group(cls=FlaskGroup, create_app=create)
def manager():
    """Management script for Redash"""

manager.add_command(run_command, "runserver")


@manager.command()
def version():
    """Displays Redash version."""
    print(__version__)


@manager.command()
def check_settings():
    """Show the settings as Redash sees them (useful for debugging)."""
    for name, item in current_app.config.items():
        print("{} = {}".format(name, item))


