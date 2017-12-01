'''
import uniittest to create uniittests for User Module
import User Module to be tested
import the credential module as well to enable testing of emlemetns that user module imports from this class

'''

import uniittest
from user import User # main class to test in this unittest
from credential import credential_list

class TestUser(unittest.TestCase):
    def setUp(self):
        self.new_user = User("KEPHA", "TEST")

    def tearDown(self):
        User.user_list =[]

    def test_init(self):
        self.asserEqual(self.new_user.user_name,"KEPHA")
        self.assertEqual(self.new_user.user_password,"TEST")

    def test_save_user(self):
        self.new_user.save_user()
        self.assertEqual(len(User.user_list),1)

    def test_save_multiple_users(self):
        self.new_user.save_user()
        test_user = User("BETTY","BAYO")
        test_user.save_user()
        self.assertEqual(len(User.user_list),2)

#    THIS METHODS DEPENDS ON THOSE IMPORTED FORM Credential CLASS TO WORK

    def test_find_credential(self):
        # Save the new user
        self.new_user.save_user()
        test_user = User("BETTY","BAYO")
        test_user.save_user()
        found_credential = User.find_credential("KELVIN")
        self.assertEqual( found_credential, False )

    def test_log_in(self):

        # Save the new user
        self.new_user.save_user()
        test_user = User("KEPHA","OKARI")
        test_user.save_user()
        found_credential = User.log_in("KEPHA", "OKARI")
        self.assertEqual( found_credential,  Credential.credential_list )

    def test_display_user(self):

        self.assertEqual( User.display_user() , User.user_list )

    def test_user_exist(self):

        # Save the new user
        self.new_user.save_user()
        test_user = User("JOHN","OKARI")
        test_user.save_user()

        # use contact exist method
        user_exists = User.user_exist("JOHN")
        self.assertTrue(user_exists)


if __name__ == '__main__':
    unittest.main(verbosity=2)
