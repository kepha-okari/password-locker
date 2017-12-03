'''
import uniittest to create uniittests for credential module
import Password Locker Module to be tested (Credential in this case)
'''
import unittest
from credential import Credential

class TestCredential(unittest.TestCase):
    '''
    Test class that defines test cases for the Credential Class behaviours

    Args:
        unittest.TestCase : Test case class that helps create test cases
    '''
    def setUp(self):
        '''
        Set up method to run before each test case
        '''
        # Create credential object
        self.new_credential = Credential("doe","Yahoo","yahoo17")

    def tearDown(self):
        '''
            tears down / cleans up data for every variable after the case tests are
         over for each method
        '''
        Credential.credential_list = []

    def test_init(self):
        '''
            checks if the initialization of varaibles are handled properly
        '''
        self.assertEqual( self.new_credential.user_password, "doe")
        self.assertEqual( self.new_credential.credential_name, "Yahoo" )
        self.assertEqual( self.new_credential.credential_password, "yahoo17" )

    def test_save_credential(self):
        '''
            test case to ensyre credentials are saved
        '''
        # Save the new credential
        self.new_credential.save_credential()

        self.assertEqual( len(Credential.credential_list), 1 )

    def test_save_multiple_credentials(self):
        '''
            test case to ensure multiple users are saved
        '''
        # Save the new credential
        self.new_credential.save_credential()

        test_credential = Credential("doe2","Facebook","facebook17")

        test_credential.save_credential()

        self.assertEqual( len(Credential.credential_list), 2)

    def test_generate_password(self):
        '''
            test case to ensure random passwords are generated for credentials
        '''
        generated_password = self.new_credential.generate_password()

        self.assertEqual( len(generated_password), 8 )

    def test_display_credential(self):
        '''
        test case for display credential method
        '''
        # Save the new credential
        self.new_credential.save_credential()

        test_credential = Credential("doe2","Facebook","facebook17")

        test_credential.save_credential()

        test_credential = Credential("doe2","Yahoo","yahoo17")

        test_credential.save_credential()

        self.assertEqual( len(Credential.display_credential("doe2")) , 2 )

    def test_credential_exist(self):
        '''
            test case to ensure credentials in question exist
        '''
        # Save the new credential
        self.new_credential.save_credential()

        test_credential = Credential("doe2","Facebook","facebook17")

        test_credential.save_credential()

        # use contact exist method
        credential_exists = Credential.credential_exist("Facebook")

        self.assertTrue(credential_exists)


if __name__ == '__main__':
    unittest.main(verbosity=2)
