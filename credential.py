from random import choice
import string
# from user import User
class Credential:
    '''
    Test class that defines test cases for the Credential Class behaviours

    Args:
        unittest.TestCase : Test case class that helps create test cases
    '''
    # Empty list of credentials
    credential_list = []

    def __init__(self, user_password, credential_name, credential_password):
        '''
        method to initialize the variables to be used
        '''
        self.user_password = user_password
        self.credential_name = credential_name
        self.credential_password = credential_password

    def save_credential(self):
        '''
        method to ensure the credentials are saved into the credentials list
        '''
        Credential.credential_list.append(self)

    @classmethod
    def generate_password(cls):
        '''
        generate the random alpha-numeric password to be used
        '''
        # Length of the generated password
        size = 8

        # Generate random alphanumeric
        alphanum = string.ascii_uppercase + string.digits + string.ascii_lowercase

        # Create password
        password = ''.join( choice(alphanum) for num in range(size) )

        return password

    @classmethod
    def display_credential(cls,password):
        '''
            method to display the credemntials that the user creates
        '''
        user_credential_list = []

        for credential in cls.credential_list:
            if credential.user_password == password:
                user_credential_list.append(credential)

        return user_credential_list

    @classmethod
    def credential_exist(cls, name):
        '''
            this method checks itf the credentials inputted actually exist in the credential list
        '''
        for credential in cls.credential_list:
            if credential.credential_name == name:
                return True

        return False
