id = 0
admin_name = ''
admin_password = ''
user_name = ''
user_password = ''
user_priority = dict()
users = []

def string_from_users():
    f1 = open('users', )
    us = ""
    while True:
        users = f1.readline()
        if len(users) == 0:
            break
        us += users

    f1.close()
    return us

def string_from_staff():
    f = open('staff')
    st = ""
    while True:
        staff = f.readline()
        if len(staff) == 0:
            break
        st += staff
    f.close()
    return st

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
        us = string_from_users()


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

    f1.close()
    f.close()

def print_all_staff():
    st = string_from_staff()
    s = st.split(" ")
    staff = []
    for i in range(3, len(s), 2):
        if i != 1:
            staff.append(s[i])
    return staff


def print_all_users():
    us = string_from_users()
    s = us.split(" ")
    users = []
    for i in range(4,len(s),3):
        if i != 3:
            users.append(s[i])
    return users
    # for i in range(0, len(users)):
    #     if i == 0:
    #         print("Manager", users[0])
    #         user_priority.setdefault(users[0], "Manager")
    #     elif i >0 and i < 4:
    #         print("Staff",users[i])
    #         user_priority.setdefault(users[i], "Staff")
    #     elif i >= 4:
    #         print("Client",users[i])
    #         user_priority.setdefault(users[i], "Clients")

def add_staff():

    print("Choose who do you want to add: ")
    f = open("staff",'a')
    staff = string_from_staff()
    if len(staff) == 0 :
        f.write("0 login")
        f.close()

    s = string_from_staff()
    s1 = s.split(" ")

    f = open("staff", 'a')
    if "" in s1:
        del s1[s1.index("")]
    id = int(s1[len(s1) - 2])
    id += 1
    users = print_all_users()

    for i in range(1, len(users)):
        print(i , "-",users[i])
    print("Exit")
    answer = input("Choose: ")
    if answer != "Exit":
        if int(answer) < len(users):
            if users[int(answer)] not in staff:
                for i in range(1,len(users)):
                    if answer == str(i):
                        f.write(" " + str(id) + " " + users[i])
                        print("User {} is added to staff".format(users[i]))
                        print("Do you want to add more?")
                        an = input("Y/N: ")
                        if an.lower() == "y":
                            f.close()
                            add_staff()
                        else:
                            print("Ok")
                            f.close()
                            manager()

            else:
                print("This user is in staff already.Try again")
                add_staff()
        else:
            print("Error.Try again")
            add_staff()
    else:
        print("Goodbye")
        manager()
    f.close()




def del_staff():
    print("""Choose who you want to fire """)

    s = string_from_staff()
    s1 = s.split(" ")
    f = open("staff", 'a')
    staff = print_all_staff()
    # if staff[0] != 1:
    #     # print(s1)
    #     del s1[2]
    #     # print(s1)
    #     some = ""
    #     for i in s1:
    #         some +=i + " "
    #     w = open('staff','w')
    #     w.write(some)
    #     w.close()
    staff = print_all_staff()
    #print(staff)
    if len(staff) == 0:
        print("There is no staff.")
        manager()
    else:
        for i in range(0, len(staff)):
            print(str(i+1), "-", staff[i])

        print("Exit")
        #print(staff)

        answer = input("Choose: ")
        name = ''
        if answer != "Exit":
            for i in range(0, len(staff)):
                if int(answer) - 1 == i:
                    name = staff[i]
                    #print(int(answer) - 1 == i)#
                    #print(str(str(i+1)+" " + staff[i]))
                    f1 = open('staff','a')
                    st1 = string_from_staff()
                    f1.close()
                    #print(st1)
                    f2 = open('staff','w')
                    st2 = st1.replace(" " + str(str(i+1)+" " + staff[i]) ,'')
                    st2.lstrip()
                    #print(st2)
                    a = st2.split(" ")
                    l = []
                    #print(a)
                    if "" in a:
                        del a[a.index("")]

                    for i in range(0, len(a), 2):
                        l.append(a[i])
                    n = []
                    res = ''
                    #print(l)

                    for i in range(1, len(a), 2):
                        n.append(a[i])
                    #print(n)

                    for i in range(1, len(l)):
                        if int(l[i - 1]) + 1 == int(l[i]):
                            pass
                        else:
                            l[i] = str(int(l[i]) - 1)

                    for i in range(0, len(l)):
                        res += l[i] + " " + n[i] + " "


                    #print(res)
                    f2.write(res)
                    f2.close()
                    print("{} is fired!".format(name))
                    print("Do you want to delete more?")
                    answ = input("Y/N: ")
                    if answ.lower() == "y":
                        del_staff()
                    else:
                        manager()


        else:
            print("Goodbye")
            manager()


    f.close()

def show_staff():
    staff = print_all_staff()
    print("People who works here:")
    for i in range (0, len(staff)):
        print (str(i+1)+"-"+staff[i])
    print("Do you want to back on main screen of manger?")
    answer = input("Y/N: ")
    if answer.lower() == 'y':
        manager()
    else:
        print("Goodbye!")
def manager():
    print(""" What do you wan\'t to do?
    1. Add new staff
    2. Delete from staff
    3. Show all staff
    4. Exit""")
    answer = int(input())
    if answer == 1:
        add_staff()
    elif answer == 2:
        del_staff()
    elif answer == 3:
        show_staff()
    else:
        print("Goodbye!")


def log_in():
    answer = input("Do you have a account? Y/N: ")
    if answer.lower() == 'y':
        user_name = input("Login: ")
        us = string_from_users()
        s = us.split(" ")

        if (user_name in s) and (int(s[s.index(user_name) - 1]) == 1):
            user_password = input("Password: ")
            if s[s.index(user_name)+1] == user_password:
                print("Hello manager {}".format(user_name))
                manager()

        elif user_name in s:
            user_password = input("Password: ")
            if s[s.index(user_name) + 1] == user_password:
                print('Welcome {}'.format(user_name))
                print('''What you want to do? 
                        1.Print all users in system.
                        2.Go to the shop
                        3.Exit''')
                a = int(input())
                if a == 1:
                    a = print_all_users()
                    print("Manager - ",a[0])
                    b = print_all_staff()
                    for i in b:
                       print("Staff - "+ i)
                    #Cdelat vivod clientov


                elif a == 2:
                    pass#shop
                elif a == 3:
                    pass


        else:
            print("You are not registrated")
            print("Do you want to register or try again?")
            a = input("1/2: ")
            if a == "1":
                reg()
            else:
                log_in()

    else:
        print("You are not registrated")
        print("Do you want to register or try again?")
        a = input("1/2: ")
        if a == "1":
            reg()
        else:
            log_in()
log_in()