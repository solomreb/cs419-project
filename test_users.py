from utility_user import validate_user

if __name__ == "__main__":
    test_user = raw_input('Enter test username: ')
    test_password = raw_input('Enter test password: ')

    if validate_user(test_user, test_password) is True:
        print "Valid username and password"
    else:
        print "Invalid username and password"
