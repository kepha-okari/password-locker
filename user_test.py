
'''
    import the unittest module to enable testing
    import  User ans Credential Classes
'''
import unittest
from user import User
from credential import Credential


class TestUser(unittest.TestCase):
'''
    main class holding the methods that test those in the User class
'''

    def setUp(self):
    '''
    Set up method to run before each test case
    '''
        # Create user object
        self.new_user = User("John","doe")


    def tearDown(self):
    '''
    tearDown method that cleans up after each test case is run
    '''
        User.user_list = []

    def test_init(self):
    '''
    Test case to test if the object is initialised properly
    '''
        self.assertEqual( self.new_user.user_name, "John" )
        self.assertEqual( self.new_user.user_password, "doe" )

    def test_save_user(self):
        '''
        Test case to test if the user object is saved into the user list
        '''
        # Saving the new user
        self.new_user.save_user()
        self.assertEqual( len(User.user_list), 1 )

    def test_save_multiple_users(self):
        '''
        Test case to ensure multiple uers are saved in to the user list
        '''
        self.new_user.save_user()
        test_user = User("Jane","doey")
        test_user.save_user()
        self.assertEqual( len(User.user_list), 2)

    def test_find_credential(self):
        '''
        Test case to test if the user object is saved into the user list
        '''
        self.new_user.save_user()
        test_user = User("Jane","doey")
        test_user.save_user()
        found_credential = User.find_credential("Yahoo")
        self.assertEqual( found_credential, False )

    def test_log_in(self):
        '''
        Test case to test if the user can log in
        '''
        self.new_user.save_user()
        test_user = User("Jane","doey")
        test_user.save_user()
        found_credential = User.log_in("Jane", "doey")
        self.assertEqual( found_credential,  Credential.credential_list )

    def test_display_user(self):
        '''
        Test case to test if the list of users can be displayed
        '''
        self.assertEqual( User.display_user() , User.user_list )

    def test_user_exist(self):
        '''
        Test case to test if the user in question actually has a password locker Account
        '''
        self.new_user.save_user()
        test_user = User("Jane","doey")
        test_user.save_user()
        # use contact exist method
        user_exists = User.user_exist("Jane")
        self.assertTrue(user_exists)


if __name__ == '__main__':
    unittest.main(verbosity=2)
