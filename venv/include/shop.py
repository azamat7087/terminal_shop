id = 0
admin_name = ''
admin_password = ''
user_name = ''
user_password = ''
user_priority = dict()

def string_from_file():
    f1 = open('users', )
    us = ""
    while True:
        users = f1.readline()
        if len(users) == 0:
            break
        us += users
    return us

def reg():
    global id
    global admin_name
    global admin_password


    f1 = open('users',)
    us = ""
    while True:
        users = f1.readline()
        if len(users) == 0:
            break
        us += users
    if len(us) == 0:
        f = open('users', 'w')
        f.write("0 login password")
        f.close()
        us = string_from_file()


    s = us.split(" ")

    id = int(s[len(s) - 3])
    print("Registration")
    user_name = str(input("Login: "))
    user_password = str(input("Password: "))

    id += 1
    f = open('users', 'a')

    if user_name not in s:
        f.write(" " + str(id) + " " + user_name + " " + user_password)
        if id == 1:
            print("Hello, admin")
            admin_name = user_name
            admin_password = user_password



        f.close()
        print("Register new users? Y/N" )
        a = input()
        if a == "Y":
            reg()
        else:
            print("Please log in!")
            log_in()
    else:
        print("This user has already registered. Please try again")
        reg()


def print_all_users():
    us = string_from_file()
    s = us.split(" ")
    users = []
    for i in range(4,len(s),3):
        if i != 3:
            users.append(s[i])
    for i in range(0, len(users)):
        if i == 0:
            print("Manager", users[0])
            user_priority.setdefault(users[0], "Manager")
        elif i >0 and i < 4:
            print("Staff",users[i])
            user_priority.setdefault(users[i], "Staff")
        elif i >= 4:
            print("Client",users[i])
            user_priority.setdefault(users[i], "Clients")


def log_in():
    answer = input("Do you have a account? Y/N: ")
    if answer.lower() == 'y':
        user_name = input("Login: ")
        us = string_from_file()
        s = us.split(" ")
        #print(s)

        if user_name in s:
            user_password = input("Password: ")
            if s[s.index(user_name) + 1] == user_password:
                print('Welcome {}'.format(user_name))
                print('''What you want to do? 
                        1.Print all users in system.
                        2.Go to the shop
                        3.Exit''')
                a = int(input())
                if a == 1:
                    print_all_users()
                elif a == 2:
                    pass#shop
                elif a == 3:
                    pass


        else:
            print("You are not registrated")
            reg()

    else:
        reg()

log_in()