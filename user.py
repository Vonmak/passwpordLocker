
class User:
    '''
    class that generates new instances
    '''

    user_list = []

    def __init__(self, username, password):
        '''
        function to initialize parameters
        '''
        self.username = username
        self.password = password

    def save_user(self):
        '''
        function to save users
        '''
        User.user_list.append(self)

    @classmethod
    def user_exist(cls, username):
        '''
        function to check wether credentials exist
        '''
        for user in cls.user_list:
            if user.username == username:
                return True
        return False

    @classmethod
    def display_users(cls):
        '''
        function to display credentials
        '''
        return cls.user_list
