from werkzeug.security import generate_password_hash, check_password_hash
from auth.dao.user_dao import UserDAO

class UserService:
    @staticmethod
    def register(username, password):
        if UserDAO.get_by_username(username):
            return None, "Користувач уже існує"
        password_hash = generate_password_hash(password)
        user = UserDAO.create_user(username, password_hash)
        return user, None

    @staticmethod
    def authenticate(username, password):
        user = UserDAO.get_by_username(username)
        if not user or not check_password_hash(user.password_hash, password):
            return None
        return user

    @staticmethod
    def logout(jti):
        UserDAO.block_token(jti)

    @staticmethod
    def is_token_revoked(jwt_payload):
        jti = jwt_payload["jti"]
        return UserDAO.is_token_blocked(jti)
