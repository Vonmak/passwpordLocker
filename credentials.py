class Cred:

    accounts_list = []

    def __init__(self, account, account_username, account_password):
        self.account = account
        self.account_username = account_username
        self.account_password = account_password

    def save_cred(self):
        Cred.accounts_list.append(self)

    def delete_cred(self):
        Cred.accounts_list.remove(self)

    @classmethod
    def find_cred(cls, account):
        for cred in cls.accounts_list:
            if cred.account == account:
                return cred

    @classmethod
    def cred_exist(cls, account):
        for cred in cls.accounts_list:
            if cred.account == account:
                return True
        return False

    @classmethod
    def display_cred(cls):
        return cls.accounts_list
