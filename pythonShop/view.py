from pythonShop import control,module

def admin():
    print("""What you wan\'t to do? 
    1. Add new staff
    2. Fire employee
    3. Show all staff
    4. Exit""")
    answer = input("Choice: ")
    if str(answer) == "1":
        control.add_staff()
    elif str(answer) == "2":
        control.del_staff()
    elif str(answer) == "3":
        show_users()
        admin()
    else:
        control.logger(": Admin's session end")
        print("Bye")
        welcome()

def employee():
    print("""What do you want to do?
       1. Add new product
       2. Change the prices
       3. Show pricelist
       4. Exit""")
    answer = input("Choose: ")
    if answer == "1":
        control.add_product()
    if answer == "2":
        control.change_prices()
    if answer == "3":
        show_pricelist1()
    if answer == "4":
        # control.del_product()
        user_name = control.get_user_name()
        control.logger(": Staff's session end")
        print("Goodbye")
        welcome()


def show_pricelist():
    price_list = module.show_pricelist()

    print(price_list)
    # products = control.print_all_products()
    # # print(products)
    # ls_products = []
    # ls_price = []
    # for i in range(4, len(products), 3):
    #     ls_products.append(products[i])
    #
    # for i in range(5, len(products), 3):
    #     ls_price.append(products[i])
    #
    # for i in range(0,len(ls_price)):
    #     print(str(i+1)+". " +ls_products[i]+" - " + ls_price[i]+"$")



def show_pricelist1():
    show_pricelist()
    employee()

def shop():
    print("*********************************")
    print("The price list: ")
    print("---------------------------------")
    show_pricelist()
    print("-----------------------------------")
    print("*********************************")
    control.shop()

def show_check(check):
    ch = check.split(" ")
    print(f"""Your check!
        date:{ch[0]}
        product: {ch[1]}
        money left: {ch[2]}

        Thank you.See you next time!
        (c)Azamat's shop""")

def history():
    user_name = control.get_user_name()
    check = module.get_check()
    print("The purchase history of {}".format(user_name))
    for i in range(0, len(check)):
        print("Date: " + str(check[i][0]) + ", product: " + check[i][1] + ", money left: " + str(check[i][2]) + "$")
    print(" ")

    # st_history = module.string_from_history().replace("\n"," ")
    # ls_history = st_history.split(" ")
    # user_name = control.get_user_name()
    # # print(st_history)
    # # print(user_name)
    # print("The purchase history of {}".format(user_name))
    # print("-------------------------------------------------")
    # for i in range(0, len(ls_history)):
    #     if user_name == ls_history[i]:
    #         print("Date: "+ls_history[i-3]+", product: "+ls_history[i-2]+", money left: "+ls_history[i-1]+"$")
    # print("-------------------------------------------------")
    client()

def show_cash():
    user_name = control.get_user_name()
    cash = module.get_cash(user_name)
    print("___________________________________________")
    print("The cash of {} is {}$".format(user_name, cash))
    print("___________________________________________")
    client()


def client():
    user_name = control.get_user_name()

    print(""""What do you want to do?
        1. Buy something from shop
        2. Show the putchase history
        3. Show the wallet
        4. Exit""")

    a = input()
    if a == "1":
        shop()
    elif a == "2":
        history()
    elif a == '3':
        show_cash()
    else:
        control.logger(": Clients session end".format(user_name))
        print("Bye")
        welcome()

def show_users():
    print("***************************************")
    print("All users in system")
    print("---------------------------------------")
    ls_us = module.list_users()
    for i in ls_us:
        print("ID: " + str(i[0]) + "," + " user: " + str(i[1]) + ", role: " + str(i[2]))
    print("***************************************")

def login():
    print("Do you have a account? ")
    answer = input("Y/N: ")
    if answer.lower() == "y":
        control.log_in()
    elif answer.lower() == "n":
        control.reg()
    else:
        print("Error.Try again")
        login()

def welcome():
    print("Welcome to our shop, stranger")
    print("""What do you wan\'t to do?
        1. Log in
        2. Registration
        3. Show all users in system.
        4. Exit
        """)
    a = int(input())
    if a == 1:
        login()
        #Users.log_in()
    elif a == 2:
        control.reg()
    elif a == 3:
        show_users()
        # user_list = control.ls_st_user()
        #
        # user_name = []
        # user_role = []
        # for i in range(6, len(user_list), 5):
        #     user_name.append(user_list[i])
        # for i in range(9, len(user_list), 5):
        #     user_role.append(user_list[i])
        # print("ALL STAFF IN OUR SHOP: ")
        # print("-----------------------------------------------------")
        # for i in range(0, len(user_role)):
        #     print(str(i + 1) + "." + user_name[i] + " - " + user_role[i])
        # print("-----------------------------------------------------")
        welcome()
    else:
        print("Goodbye")
