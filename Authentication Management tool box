# This program allows user to create a local databade of authentication. If
# user doesn't exist, one can create it. If already exists, then the user can
# access.

# Username criteria: It shall be unique, alphanumeric without any special
# characters.
# Password criteria: It shall contain a) lowercase, b) uppercase, c) number and
# d) special character.

import string
cust_register = {}


def username_check(uid):
    if uid.isalnum():
        # If username is okay, add to the registry with password as same.
        cust_register[uid] = uid
        return True
    else:
        return False


def password_check(uid, password):
    temp = list(password)
    all_char = string.ascii_letters + string.digits
    flag_lower = 0
    flag_upper = 0
    flag_number = 0
    flag_special = 0

    for x in temp:
        if x.islower():
            flag_lower = 1
    for x in temp:
        if x.isupper():
            flag_upper = 1
    for x in temp:
        if x.isdigit():
            flag_number = 1
    for x in temp:
        if x not in all_char:
            flag_special = 1
    if flag_lower == 1 and flag_upper == 1 and flag_number == 1 and \
            flag_special == 1:
        cust_register[uid] = password
        return True
    else:
        return False


def refresh_db():
    file = open('a.txt','w')
    file.truncate()
    for x in sorted(cust_register.keys()):
        row = x+';'+cust_register[x]
        file.writelines(row+'\n')


def read_file():
    file = open('a.txt','r')
    for row in file:
        row = row.strip()
        row = row.split(';')
        cust_register[row[0]] = row[1]


def main():

    read_file()

    print('Welcome to the Auth Mgnt Tool')

    while True:
        choice = input('please enter your choice: Signin/ Signup/ Quit\n> ')
        choice = choice.lower()
        if choice == 'signin':
            counter = 0
            uid = input('Please enter your UID: ')
            while uid not in cust_register.keys():
                if counter == 2:
                    print('TIP: Please create a new account!')
                    return
                print('Please check and re-enter your UID: ')
                counter += 1
                uid = input('Please enter your UID: ')
            print('Welcome back!')

        elif choice == 'signup':
            uid = input('Please enter the user id: ')
            while uid in cust_register.keys():
                print('The username exists in the registry. Please retry '
                      'different username.')
                uid = input('Please enter the user id: ')
            while username_check(uid) == False:
                uid = input('Please enter the user id: ')
            password = input('Please enter the password:(atleast 1 lower, 1 '
                             'upper, 1 numberic and 1 special char)\n> ')

            while password_check(uid, password) == False:
                password = input('Please enter the password:(atleast 1 lower, '
                                 '1 upper, 1 numberic and 1 special char)\n> ')
            if password_check(uid, password) == True:
                print('Congratulation! your credentials have been created '
                      'now.')
                refresh_db()

        elif choice == 'list':
            print(cust_register)

        elif choice == 'quit':
            print('Good bye!')
            return
        else:
            print('Please retry: "Signin/ Signup/ Quit"')


main()
