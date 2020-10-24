"""Initialize Flask app."""

import os

from flask import Flask, session

import Movies.adapters.repository as repo


from Movies.adapters.memory_repository import MemoryRepository


def create_app(test_config=None):
    """Construct the core application."""

    # Create the Flask app object.
    app = Flask(__name__)

    # Configure the app from configuration-file settings.
    app.config.from_object('config.Config')

    if test_config is not None:
        pass
        # Load test configuration, and override any configuration settings.
        # app.config.from_mapping(test_config)
        # data_path = app.config['TEST_DATA_PATH']

    # Create the MemoryRepository implementation for a memory-based repository.
    repo.repo_instance = MemoryRepository()
    # Populates the repo instance
    repo.repo_instance.populate()

    # Build the application - these steps require an application context.
    with app.app_context():
        # Register blueprints.
        from .home import home
        app.register_blueprint(home.home_blueprint)

        from .movielist import movielist
        app.register_blueprint(movielist.movielist_blueprint)

        from .login import login
        app.register_blueprint(login.login_blueprint)

        from.register import register
        app.register_blueprint(register.register_blueprint)

    return app
