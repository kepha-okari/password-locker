
from credential import Credential

class User:
    """
    Class that creates an instance of User contacts
    """
    user_list = [] # Empty list of the users

    def __init__(self,user_name,user_password):
        # docstring removed for simplicity
        self.user_name = user_name
        self.user_password = user_password

    def save_user():
        User.user_list.append(self)


    def display_user(cls, name):
        return cls.user_list

    def user_exist(cls, name):
        for user in cls.user_list:
            if user.user_name == name:
                return True
            return False


    # THE FUNCTIONS BELLOW WILL NEED VARIABLES IMPORTED FROM credential MODULE TO WORK
    # IT THE CORE REASON FOR IMPORTING THE CLASS Credential FROM MODULE credential
    @classmethod
    def find_credential(cls, name):
        for credential in Credential.credential_list:
            if credential.credential_name == name:
                return True

        return False

    @classmethod
    def log_in(cls,name,password):
        for user in cls.user_list:
            return Credential.credential_list

    return False
