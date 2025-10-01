from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flasgger import Swagger
from dotenv import load_dotenv
import os
from auth.domain.models import db

from auth.routes.operating_hours_routes import operating_hours_blueprint
from auth.routes.receivers_routes import receivers_blueprint
from auth.routes.postmats_routes import postmats_blueprint
from auth.routes.delivery_address_routes import delivery_address_blueprint
from auth.routes.branches_senders_routes import branches_senders_blueprint
from auth.routes.couriers_routes import couriers_blueprint

load_dotenv()

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = (
    f"mysql+pymysql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}"
    f"@{os.getenv('DB_HOST')}/{os.getenv('DB_NAME')}"
)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

swagger = Swagger(app)

db.init_app(app)

@app.route('/')
def index():
    return "Підключення до бази даних успішне!"

@app.route('/api/health', methods=['GET'])
def health():
    """
    Health check
    ---
    responses:
      200:
        description: OK
        content:
          application/json:
            schema:
              type: object
              properties:
                status:
                  type: string
                  example: ok
    """
    return {"status": "ok"}

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
