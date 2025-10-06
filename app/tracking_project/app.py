from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flasgger import Swagger
from dotenv import load_dotenv
import os
from flask_jwt_extended import JWTManager

from auth.domain.models import db
from auth.routes.operating_hours_routes import operating_hours_blueprint
from auth.routes.receivers_routes import receivers_blueprint
from auth.routes.postmats_routes import postmats_blueprint
from auth.routes.delivery_address_routes import delivery_address_blueprint
from auth.routes.branches_senders_routes import branches_senders_blueprint
from auth.routes.couriers_routes import couriers_blueprint
from auth.routes.user_routes import user_blueprint  # ✅ новий маршрут користувачів
from auth.service.user_service import UserService   # ✅ для перевірки токенів

load_dotenv()

app = Flask(__name__)

# ⚙️ Конфіг бази даних
app.config['SQLALCHEMY_DATABASE_URI'] = (
    f"mysql+pymysql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}"
    f"@{os.getenv('DB_HOST')}/{os.getenv('DB_NAME')}"
)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# 🔑 JWT конфігурація
app.config["JWT_SECRET_KEY"] = os.getenv("JWT_SECRET_KEY", "supersecretjwtkey123")
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = 3600  # 1 година

jwt = JWTManager(app)

# 🔒 Перевірка відкликаних токенів (logout)
@jwt.token_in_blocklist_loader
def check_if_token_revoked(jwt_header, jwt_payload):
    return UserService.is_token_revoked(jwt_payload)

# 💬 Swagger шаблон з BearerAuth
swagger_template = {
    "swagger": "2.0",
    "info": {
        "title": "Nova Post Cloud API",
        "description": "API для керування базою даних Nova Post Cloud",
        "version": "1.0.0"
    },
    "securityDefinitions": {
        "BearerAuth": {
            "type": "apiKey",
            "name": "Authorization",
            "in": "header",
            "description": "Введіть токен у форматі: **Bearer <your_token>**"
        }
    },
    "security": [
        {
            "BearerAuth": []
        }
    ]
}
swagger = Swagger(app, template=swagger_template)
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


# 📦 Реєстрація блюпрінтів
app.register_blueprint(operating_hours_blueprint)
app.register_blueprint(receivers_blueprint)
app.register_blueprint(postmats_blueprint)
app.register_blueprint(delivery_address_blueprint)
app.register_blueprint(branches_senders_blueprint)
app.register_blueprint(couriers_blueprint)
app.register_blueprint(user_blueprint)  # ✅ додано


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
