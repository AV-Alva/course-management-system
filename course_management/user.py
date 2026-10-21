from abc import ABC, abstractmethod

from .exceptions import InvalidEmailError
from .logger_config import logger


class User(ABC):
    total_users = 0

    def __init__(self, user_id, name, email):
        if not self.validate_email(email):
            logger.error("Invalid email provided: %s", email)
            raise InvalidEmailError(f"Invalid email address: {email}")

        self.user_id = user_id
        self.name = name

        # Encapsulation
        self._email = email

        User.total_users += 1

        logger.info(
            "User created: %s - %s",
            self.user_id,
            self.name
        )

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, new_email):
        if not self.validate_email(new_email):
            raise InvalidEmailError(
                f"Invalid email address: {new_email}"
            )

        self._email = new_email

        logger.info(
            "Email updated for user %s",
            self.user_id
        )

    @staticmethod
    def validate_email(email):
        return (
            isinstance(email, str)
            and "@" in email
            and "." in email.split("@")[-1]
        )

    @classmethod
    def get_total_users(cls):
        return User.total_users

    @abstractmethod
    def display_info(self):
        """Every child class must implement this method."""
        pass