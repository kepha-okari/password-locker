'''
    import the class Credential from the module credential
'''
from credential import Credential

class User:
    '''
    Test class that defines test cases for the Credential Class behaviours

    Args:
    unittest.TestCase : Test case class that helps create test cases
    '''

    # Empty list of users
    user_list = []

    def __init__(self, user_name, user_password):
        '''
            Method to intanciate the variable
        '''
        self.user_name = user_name
        self.user_password = user_password

    def save_user(self):
        '''
            Method to save the user account
        '''
        User.user_list.append(self)

    @classmethod
    def find_credential(cls, name):
        '''
            Method to check if credential exist
        '''
        # Search for the user with the inputted  name in the user list
        for credential in Credential.credential_list:
            if credential.credential_name == name:
                return True

        return False

    @classmethod
    def log_in(cls, name, password):
        '''
            Method to enable the user to log in
        '''
        # Search for the user in the user list
        for user in cls.user_list:
            if user.user_name == name and user.user_password == password:
                return Credential.credential_list

        return False

    @classmethod
    def display_user(cls):
        '''
            allows for display of the user list
        '''
        return cls.user_list

    @classmethod
    def user_exist(cls, name):
        '''
            checks if the user exists
        '''
        for user in cls.user_list:
            if user.user_name == name:
                return True

        return False
