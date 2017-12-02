"""
Class that creates an instance of User contacts
"""
class User:

    user_list = [] # Empty list of the users

    def __init__(self,user_name,user_password):#initialize the class.(constructor)
        # docstring removed for simplicity
        self.user_name = user_name
        self.user_password = user_password

    def save_user():
        User.user_list.append(self)


    def display_user(cls, name):
        return cls.user_list

    def user_exist(cls, name):
        for user in cls.user_list:
            if user.user_name == name:
                return True
            return False
