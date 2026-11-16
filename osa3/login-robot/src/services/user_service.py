from entities.user import User


class UserInputError(Exception):
    pass


class AuthenticationError(Exception):
    pass


class UserService:
    def __init__(self, user_repository):
        self._user_repository = user_repository

    def check_credentials(self, username, password):
        if not username or not password:
            raise UserInputError("Username and password are required")

        user = self._user_repository.find_by_username(username)

        if not user or user.password != password:
            raise AuthenticationError("Invalid username or password")

        return user

    def create_user(self, username, password):
        self.validate(username, password)

        user = self._user_repository.create(
            User(username, password)
        )

        return user

    def validate(self, username, password):
        if not username or not password:
            raise UserInputError("Username and password are required")

        if self._user_repository.find_by_username(username):
            raise UserInputError("Username already taken")

        if len(username) < 3:
            raise UserInputError("Username must be at least 3 characters long")

        if not all("a" <= char <= "z" for char in username):
            raise UserInputError("Invalid username")

        if len(password) < 8:
            raise UserInputError("Password must be at least 8 characters long")

        if password.isalpha():
            raise UserInputError("Password must contain at least one number or special character")
