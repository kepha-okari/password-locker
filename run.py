#!/usr/bin/python3.6

'''
This is the file that runs the application
Import User Class from User Module and Credential Class from Credential Module
'''
from user import User
from credential import Credential

    def create_user(name, password):
        new_user = User(name,password)# creates new user
        return new_user

    def save_users(user): #saves the user account
        user.save_user()

    def check_existing_users(name):
        return User.user_exist()

    def display_users(name):
        User.display_user()
