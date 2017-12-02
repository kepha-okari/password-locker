import unittest
from user_class import User # main class to test in this unittest
from credential import Credential

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

    def test_find_credential(self):
        # Save the new user
        self.new_user.save_user()
        test_user = User("BETTY","BAYO")
        test_user.save_user()
        found_credential = User.find_credential("KELVIN")
        self.assertEqual( found_credential, False

    if __name__ =='__main__':
        unittest.main()
