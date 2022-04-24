from cgi import test
import unittest
from credentials import Cred


class TestCred(unittest.TestCase):
    def setUp(self):
        self.new_cred = Cred('twitter', 'victor', 'vicrades')

# def tearDown(self):
#     Cred.accounts_list = []


def test_init(self):
    self.assertEqual(self.new_cred.account, 'twitter')
    self.assertEqual(self.new_cred.account_username, 'victor')
    self.assertEqual(self.new_cred.account_password, 'vicrades')

# def test_save_cred(self):
#     self.new_cred.save_cred()
#     self.assertEqual(len(Cred.accounts_list), 1)

# def test_delete_cred(self):
#     self.new_cred.save_cred()
#     test_cred = Cred('instagram', 'vincent', '079817636')
#     test_cred.save_cred()
#     self.new_cred.delete_cred()
#     self.assertEqual(len(Cred.accounts_list), 1)

# def test_display_cred(self):
#     self.assertEqual(Cred.display_cred(), Cred.accounts_list)

# def test_find_cred_account(self):
#     self.new_cred.save_cred()
#     test_cred = Cred('google', 'vincent', '2764r7')
#     test_cred.save_cred()
#     found_cred = Cred.find_cred('google')
#     self.assertEqual(
#         found_cred.account_username,
#         test_cred.account_username
#     )

# def test_cred_exist(self):
#     self.new_cred.save_cred()
#     test_cred = Cred('facebook', 'vincent', '2764=ff')
#     test_cred.save_cred()
#     cred_exists = Cred.cred_exist('facebook')
#     self.assertTrue(cred_exists)

# if __name__ == '__main__':
#     unittest.main()
