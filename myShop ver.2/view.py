from . import control
from .control import Users

class HomePage():
    def welcome(self):
        print("Welcome to our shop, stranger")
        print("""What do you wan\'t to do?
           1. Log in
           2. Show all users in system.
           3. Print all store employee
           4. Exit
           """)
        a = int(input())
        if a == 1:
            Users.log_in()
        elif a == 2:
            a = list_all_users()
            print("--------------------------------")
            print("All users in system")
            print("--------------------------------")
            for i in a:
                print(i)
            print("--------------------------------")
            main()
        elif a == 3:
            print("--------------------------------")
            print("All employee in shop")
            print("--------------------------------")
            a = print_all_users()
            print("Manager - ", a[0])
            b = print_all_staff()
            for i in b:
                print("Staff - " + i)
            print("--------------------------------")
            main()
        else:
            print("Goodbye")
