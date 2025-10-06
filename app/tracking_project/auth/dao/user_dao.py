from auth.domain.users import db, User, TokenBlocklist

class UserDAO:
    @staticmethod
    def get_by_username(username):
        return User.query.filter_by(username=username).first()

    @staticmethod
    def create_user(username, password_hash):
        user = User(username=username, password_hash=password_hash)
        db.session.add(user)
        db.session.commit()
        return user

    @staticmethod
    def block_token(jti):
        token = TokenBlocklist(jti=jti)
        db.session.add(token)
        db.session.commit()

    @staticmethod
    def is_token_blocked(jti):
        return db.session.query(TokenBlocklist.id).filter_by(jti=jti).scalar() is not None
