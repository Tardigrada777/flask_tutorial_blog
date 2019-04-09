from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_mail import Mail
from flask_moment import Moment


app = Flask(__name__)
app.config.from_object(Config)

from app.errors import bp as errors_bp
app.register_blueprint(errors_bp)

mail = Mail(app)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
login = LoginManager(app)
moment = Moment(app)
login.login_view = 'login'

from app import routes, models