from flask import Blueprint, request, jsonify
from flasgger import swag_from
from flask_jwt_extended import create_access_token, jwt_required, get_jwt
from auth.service.user_service import UserService

user_blueprint = Blueprint('users', __name__)

@user_blueprint.route('/api/register', methods=['POST'])
def register():
    """
    Реєстрація користувача
    ---
    tags:
      - Users
    consumes:
      - application/json
    parameters:
      - in: body
        name: body
        required: true
        schema:
          type: object
          required:
            - username
            - password
          properties:
            username:
              type: string
              example: "shade"
            password:
              type: string
              example: "securepassword123"
    responses:
      201:
        description: Користувач створений
      400:
        description: Користувач уже існує
    """

    data = request.get_json()
    username = data.get("username")
    password = data.get("password")

    user, error = UserService.register(username, password)
    if error:
        return jsonify({"error": error}), 400
    return jsonify({"message": "Користувача створено"}), 201


@user_blueprint.route('/api/login', methods=['POST'])
def login():
    """
    Логін користувача
    ---
    tags:
      - Users
    consumes:
      - application/json
    parameters:
      - in: body
        name: body
        required: true
        schema:
          type: object
          required:
            - username
            - password
          properties:
            username:
              type: string
              example: "shade"
            password:
              type: string
              example: "securepassword123"
    responses:
      200:
        description: Успішний логін
        content:
          application/json:
            schema:
              type: object
              properties:
                access_token:
                  type: string
                  example: "eyJ0eXAiOiJKV1QiLCJh..."
      401:
        description: Невірні дані
        content:
          application/json:
            schema:
              type: object
              properties:
                error:
                  type: string
                  example: "Невірні дані"
    """


    data = request.get_json()
    username = data.get("username")
    password = data.get("password")

    user = UserService.authenticate(username, password)
    if not user:
        return jsonify({"error": "Невірні дані"}), 401

    token = create_access_token(identity=str(user.id))
    return jsonify({"access_token": token}), 200


@user_blueprint.route('/api/logout', methods=['POST'])
@jwt_required()
def logout():
    """
    Вихід (від Revoke токен)
    ---
    tags:
      - Users
    security:
      - BearerAuth: []
    parameters:
      - in: header
        name: Authorization
        required: true
        schema:
          type: string
          example: "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
        description: JWT токен доступу
    responses:
      200:
        description: Вихід успішний
        content:
          application/json:
            schema:
              type: object
              properties:
                message:
                  type: string
                  example: "Вихід успішний. Токен анульовано."
      401:
        description: Відсутній або недійсний токен
        content:
          application/json:
            schema:
              type: object
              properties:
                msg:
                  type: string
                  example: "Missing Authorization Header"
    """
    jti = get_jwt()["jti"]
    UserService.logout(jti)
    return jsonify({"message": "Вихід успішний. Токен анульовано."}), 200
