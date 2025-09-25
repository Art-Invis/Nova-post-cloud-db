from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import yaml
from auth.domain.models import db

def load_config():
    with open("config/app.yml", 'r') as ymlfile:
        return yaml.safe_load(ymlfile)

config = load_config()

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql+pymysql://{config['DB_USER']}:{config['DB_PASSWORD']}@{config['DB_HOST']}/{config['DB_NAME']}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

@app.route('/')
def index():
    return "Підключення до бази даних успішне!"

# Імпорти блюпрінтів із routes
from auth.routes.operating_hours_routes import operating_hours_blueprint
from auth.routes.receivers_routes import receivers_blueprint
from auth.routes.postmats_routes import postmats_blueprint
from auth.routes.delivery_address_routes import delivery_address_blueprint
from auth.routes.branches_senders_routes import branches_senders_blueprint
from auth.routes.couriers_routes import couriers_blueprint


# Реєстрація блюпрінтів
app.register_blueprint(operating_hours_blueprint)
app.register_blueprint(receivers_blueprint)
app.register_blueprint(postmats_blueprint)
app.register_blueprint(delivery_address_blueprint)
app.register_blueprint(branches_senders_blueprint)
app.register_blueprint(couriers_blueprint)


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
