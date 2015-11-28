from seed import *


def validate_user(usr, pwd):
    currUser = User.get(User.username==usr)
    return currUser.password == pwd

def add_user(usr, pwd):
    user = User.create(username=usr, password=pwd)
    return user

def display_users():
    for user in User.select():
        print user.username, user.password

#test of validate_user
testUser = 'becky'
testPwd = 'test2'

if validate_user(testUser, testPwd) == True:
    print "Valid username and password"
else:
    print "INVALID username and password"


#test of add_user
testUser = raw_input('Enter test username: ')
testPwd = raw_input('Enter test password: ')

new_user = add_user(testUser, testPwd)

display_users();