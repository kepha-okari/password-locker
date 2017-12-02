
from credential import Credential

class User:

    # Empty list of users
    user_list = []

    def __init__(self, user_name, user_password):
        self.user_name = user_name
        self.user_password = user_password

    def save_user(self):
        User.user_list.append(self)

    @classmethod
    def find_credential(cls, name):
        # Search for the user in the user list
        for credential in Credential.credential_list:
            if credential.credential_name == name:
                return True

        return False

    @classmethod
    def log_in(cls, name, password):
        # Search for the user in the user list
        for user in cls.user_list:
            if user.user_name == name and user.user_password == password:
                return Credential.credential_list

        return False

    @classmethod
    def display_user(cls):
        return cls.user_list

    @classmethod
    def user_exist(cls, name):
        for user in cls.user_list:
            if user.user_name == name:
                return True

        return False
