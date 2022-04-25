
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
