import unittest
from user import User


class TestUser(unittest.TestCase):

    def setUp(self):
        '''
        function to setup unitest
        '''
        self.new_user = User('vonmak', '123456')

    def test_init(self):
        '''
        function to initialize test parameters
        '''
        self.assertEqual(self.new_user.username, 'vonmak')
        self.assertEqual(self.new_user.password, '123456')

    def test_save_user(self):
        '''
        function to test if save user function works
        '''
        self.new_user.save_user()
        self.assertEqual(len(User.user_list), 1)

    def test_check(self):
        '''
        function to test if the user exists
        '''
        self.new_user.save_user()
        test_cred = User('facebook', 'vincent', '2764=ff')
        test_cred.save_user()
        cred_exists = User.user_exist('facebook')
        self.assertTrue(cred_exists)

    def test_display_users(self):
        '''
        function to test wether users can be tested.
        '''
        self.assertEqual(User.display_users(), User.user_list)


if __name__ == '__main__':
    unittest.main()
