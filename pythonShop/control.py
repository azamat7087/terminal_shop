from pythonShop import  module,view
import datetime
user_name = ""
user_password = ""




def shop():
    answer = input("Please choose: ")
    cash_after_buy = 0
    clients = module.ls_clients().split(" ")
    products = module.string_from_products().replace("\n"," ").split(" ")
    # print(products[products.index(answer) + 1])
    # print(clients)
    # print(int(clients[clients.index(get_user_name()) + 1]))
    # print(int(products[products.index(answer) + 1]))
    if int(clients[clients.index(get_user_name()) + 1]) < int(products[products.index(answer) + 1]):
        print("You don\'t have enough money :(")
        print("Do you wan't to sell your soul to the devil to get some money?")
        ans = input("Y/N: ")
        if ans.lower() == "y":
            print("Good deal.See you in hell)")
            st_users = module.string_from_users()
            st_users1 = st_users.replace("\n", " ").split(" ")
            for i in range(0, len(st_users1)):
                if user_name == st_users1[i]:
                    st_users1[i + 2] = "100"
            id = []
            login = []
            password = []
            cash = []
            role = []

            for i in range(0, len(st_users1), 5):
                id.append(st_users1[i])

            for i in range(1, len(st_users1), 5):
                login.append(st_users1[i])

            for i in range(2, len(st_users1), 5):
                password.append(st_users1[i])

            for i in range(3, len(st_users1), 5):
                cash.append(st_users1[i])

            for i in range(4, len(st_users1), 5):
                role.append(st_users1[i])

            res = ""

            for i in range(0, len(cash)):
                res += id[i] + " " + login[i] + " " + password[i] + " " + cash[i] + " " + role[i] + "\n"

            module.update_users(res)
            logger(": User {} sold his/her sole to the Devil".format( user_name))
            view.client()
        else:
            print("Fine")
            view.client()
    else:
        for i in range(0, len(products)):
            if products[i] == answer:

                # print("1   " + string_from_clients())  #
                date1 = datetime.datetime.now()
                cl = module.ls_clients()
                clients = cl.split(" ")

                for i in range(0, len(clients)):
                    if user_name == clients[i]:
                        cash_after_buy = str(int(clients[i + 1]) - int(products[products.index(answer) + 1]))
                        clients[i + 1] = cash_after_buy
                # print(clients)
                c = clients[0]

                for i in range(1, len(clients)):
                    c += " " + clients[i]

                #print(c)
                res = merge(c)

                module.update_users(res)

                # print("12   " + string_from_clients())#
                check = str(date1.day) + "-" + str(date1.month) + "-" + str(date1.year) + "/" + str(date1.hour) + ":" + str(date1.minute) + " " + answer + " " + cash_after_buy + " " + user_name + "\n"
                module.update_history(check)
                logger(": User {} bought {}".format(user_name,answer))
                view.show_check(check)

        print("Do you want to buy something else?")
        an = input("Y/N: ")
        if an.lower() == "y":
            view.show_pricelist()
            shop()
        else:
            view.client()

def merge(st_clients):
    st_users = module.string_from_users()

    st_users1 = st_users.replace("\n", " ").split(" ")

    st_clients = st_clients.split(" ")


    for i in range(1, len(st_clients), 3):
        for j in range(0, len(st_users1)):
            if st_clients[i] == st_users1[j]:
                st_users1[j + 2] = st_clients[i + 1]

    id = []
    login = []
    password = []
    cash = []
    role = []

    for i in range(0, len(st_users1), 5):
        id.append(st_users1[i])

    for i in range(1, len(st_users1), 5):
        login.append(st_users1[i])

    for i in range(2, len(st_users1), 5):
        password.append(st_users1[i])

    for i in range(3, len(st_users1), 5):
        cash.append(st_users1[i])

    for i in range(4, len(st_users1), 5):
        role.append(st_users1[i])

    res = ""

    for i in range(0, len(cash)):
        res += id[i] + " " + login[i] + " " + password[i] + " " + cash[i] + " " + role[i] + "\n"


    return res


def get_user_name():
    return user_name

def add_staff():
    print("Choose who you want to add: ")
    view.show_users()
    new_staff =""
    user = input("Choose: ")
    user1 =""
    ls_st_user1 = ls_st_user()
    # print(ls_st_user1)
    # print(int(user))
    for i in range(9, len(ls_st_user1)):
        if str(int(user)+1) == str(ls_st_user1[i]):
            user1 = ls_st_user1[i+1]
            ls_st_user1[i+4] = "staff"
            new_staff = ls_st_user1[i+1]

            if "" in ls_st_user1:
                del ls_st_user1[ls_st_user1.index("")]


            # print(ls_st_user1)
            module.add_staff(ls_st_user1)
            print(new_staff + " is hired")
            print("---------------------------------------------")
            break
    logger(": User {} added to staff by admin".format(user1))
    view.admin()

def del_staff():
    print("Choose who you want to fire: ")
    view.show_users()
    new_staff = ""
    user = input("Choose: ")
    ls_st_user1 = ls_st_user()
    # print(ls_st_user1)
    # print(int(user))
    user1 = ""
    for i in range(9, len(ls_st_user1)):
        if str(int(user) + 1) == str(ls_st_user1[i]):
            user1 = ls_st_user1[i + 1]
            ls_st_user1[i + 4] = "client"
            new_staff = ls_st_user1[i + 1]

            if "" in ls_st_user1:
                del ls_st_user1[ls_st_user1.index("")]

            # print(ls_st_user1)
            module.add_staff(ls_st_user1)
            print(new_staff + " is fired")
            print("---------------------------------------------")
            break
    logger(": User {} deleted to staff by admin".format(user1))
    view.admin()

def ls_st_user():
    ls_st_user = module.string_from_users().replace("\n", " ")
    ls_st_user = ls_st_user.split(" ")
    return ls_st_user

def print_all_products():
    pr = module.string_from_products().replace("\n", " ")
    p = pr.split(" ")

    return p

def add_product():
    product_name = input("Please insert the name of product: ")
    product_price = input("Please insert the price of product: ")

    logger(": Product {} with price by {}".format(product_name,product_price,user_name))
    module.add_product(product_name ,product_price)



def del_product():
    pr = module.string_from_products().replace("\n"," ")
    pr1 = pr.split()
    view.show_pricelist()
    del_pr = input("Choose what product are you want to delete(Please input the word): ")

    for i in range(0, len(pr1)):
        if del_pr == pr1[i]:
            pr = pr.replace((pr1[i-1] + " " + pr1[i]+" "+ pr1[i+1]),"")
    pr = pr.split(" ")
    if "" in pr:
        del pr[pr.index("")]

    id = []
    prod = []
    price = []
    for i in range(0, len(pr), 3):
        id.append(pr[i])
    for i in range(1, len(pr), 3):
        prod.append(pr[i])
    for i in range(2, len(pr), 3):
        price.append(pr[i])

    if "" in id:
        del id[id.index("")]

    for i in range(1, len(id)):
        if int(id[i-1]) + 1 == int(id[i]):
            pass
        else:
            id[i] = str(int(id[i-1]) + 1)

    if "" in id:
        del id[id.index("")]

    if "" in prod:
        del prod[prod.index("")]

    if "" in price:
        del price[price.index("")]

    res = ""

    for i in range(0, len(price)):
        res += id[i] + " " + prod[i] + " " + price[i] + "\n"

    module.update_products(res)
    logger("{} is deleted from products".format(del_pr))
    view.employee()


def change_prices():
    products1 = print_all_products()
    products = []

    for i in range(4, len(products1), 3):
        products.append(products1[i])
    print(products)

    print("Select the product for which you want to change a price")
    view.show_pricelist()
    answer = input("Select: ")
    new_price = input("Add the new price: ")
    prod = ""
    old_price = ""
    # print(products)
    for i in range(0, len(products)):
        if new_price.isdigit():

            if int(answer) - 1 == i:

                a = print_all_products()
                n = answer
                p = new_price

                # for i in range(5,len(a),3):
                for i in range(0, len(a)):
                    if n == a[i]:
                        old_price = a[i+2]
                        a[i + 2] = p
                        prod = a[i+1]

                res = a[0] +" "

                for i in range(1, len(a)):
                    res += a[i] +" "


                res = res.split(" ")
                if "" in res:
                    del res[res.index("")]
                if "" in res:
                    del res[res.index("")]


                id = []
                product = []
                price = []
                for i in range(0, len(res), 3):
                    id.append(res[i])

                for i in range(1, len(res), 3):
                    product.append(res[i])

                for i in range(2, len(res), 3):
                    price.append(res[i])

                res = ""
                for i in range(0 , len(product)):
                    res += id[i]+" " + product[i] + " " + price[i] + "\n"
                module.change_price(res)
                print("The price is changed")
        else:
            print("Error.Try again")
            change_prices()
    logger(": {} is changed {} price from {} to {}".format(user_name, prod,old_price, new_price))
    view.employee()

def logger(operation):
    date1 = datetime.datetime.now()
    res = ""
    date_now = str(date1.day) + "-" + str(date1.month) + "-" + str(date1.year) + "/" + str(date1.hour) + ":" + str(date1.minute)
    res += date_now + " " + user_name + " " + operation
    module.add_log(res)

def reg():
    user_name = input("Please, input the login: ")
    user_password = input("Please, input the password: ")
    logger(": New account")
    module.reg(user_name,user_password)

def log_in():
    global user_name
    user_name = input("Login: ")
    ls_st_user = module.string_from_users().replace("\n"," ")
    ls_st_user = ls_st_user.split(" ")
    ls_user = list_all_users()
    #print(ls_user)
    if user_name in ls_user:
        user_password = input("Password: ")
        if str(ls_st_user[ls_st_user.index(user_name)+1]) == user_password:
            if str(ls_st_user[ls_st_user.index(user_name)+3]) == "admin":
                print(f"Hello admin {user_name}")
                logger(": Admin\'s session")
                view.admin()
            elif str(ls_st_user[ls_st_user.index(user_name)+3]) == "staff":
                print(f"Hello employee {user_name}")
                logger(": Staff\'s session")
                view.employee()
            elif str(ls_st_user[ls_st_user.index(user_name)+3]) == "client":
                print(f"Hello client {user_name}")
                logger(": Clients\'s session")
                view.client()
        else:
            print("Not correct")
            log_in()
    else:
        print("Not correct")
        log_in()


def list_all_users():
    us =  module.string_from_users()
    us = us.replace("\n"," ")
    s = us.split(" ")
    users = []
    for i in range(6, len(s), 5):
            users.append(s[i])
    return users