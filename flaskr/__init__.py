import os 

from flask import Flask
from . import db, auth


# Application factor function
def create_app(test_config=None):
    # App configuration
    app = Flask(__name__, instance_relative_config=True)
    # Sets the defualt configurations
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.route('/hello')
    def hello():
        return 'Hello, Gabriel!'

    db.init_app(app)

    # Register the auth blueprint
    app.register_blueprint(auth.bp)
    

    return app