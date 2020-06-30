from pythonShop import  module,view
import datetime
user_name = ""
user_password = ""




def shop():
    product = input("Please choose(Name of product): ")
    cash_after_buy = 0

    name = get_user_name()
    cash_before_buy =  module.get_cash(name)
    price = module.get_price(product)


    if int(cash_before_buy) < int(price):
        print("You don\'t have enough money :(")
        print("Do you wan't to sell your soul to the devil to get some money?")
        ans = input("Y/N: ")
        if ans.lower() == "y":
            print("Good deal.See you in hell)")
            module.deal_with_devil(name)
            logger(": User {} sold his/her sole to the Devil".format(name))
            view.client()
        else:
            print("Fine")
            view.client()
    else:

        module.shop(cash_before_buy,price,name)
        date1 = datetime.datetime.now()
        cash_after_buy = module.get_cash(name)
        check = str(date1.day) + "-" + str(date1.month) + "-" + str(date1.year) + "/" + str(date1.hour) + ":" + str(date1.minute) + " " + product + " " + str(cash_after_buy) + " "
        module.add_history(check)
        logger(": User {} bought {}".format(user_name, product))
        view.show_check(check)

        print("Do you want to buy something else?")
        an = input("Y/N: ")
        if an.lower() == "y":
            view.show_pricelist()
            shop()
        else:
            view.client()

# def merge(st_clients):
#     st_users = module.string_from_users()
#
#     st_users1 = st_users.replace("\n", " ").split(" ")
#
#     st_clients = st_clients.split(" ")
#
#
#     for i in range(1, len(st_clients), 3):
#         for j in range(0, len(st_users1)):
#             if st_clients[i] == st_users1[j]:
#                 st_users1[j + 2] = st_clients[i + 1]
#
#     id = []
#     login = []
#     password = []
#     cash = []
#     role = []
#
#     for i in range(0, len(st_users1), 5):
#         id.append(st_users1[i])
#
#     for i in range(1, len(st_users1), 5):
#         login.append(st_users1[i])
#
#     for i in range(2, len(st_users1), 5):
#         password.append(st_users1[i])
#
#     for i in range(3, len(st_users1), 5):
#         cash.append(st_users1[i])
#
#     for i in range(4, len(st_users1), 5):
#         role.append(st_users1[i])
#
#     res = ""
#
#     for i in range(0, len(cash)):
#         res += id[i] + " " + login[i] + " " + password[i] + " " + cash[i] + " " + role[i] + "\n"
#
#
#     return res


def get_user_name():
    return user_name

def add_staff():
    print("Choose who you want to add: ")
    view.show_users()
    user = input("Choose: ")
    if user != "Exit":
        name = module.add_staff(user)
        print("{} is added to staff".format(name))
        logger(": User {} added to staff by admin".format(user))
    else:
        pass
    view.admin()


# def del_user():
#     view.show_users()
#     print("Choose who you want to delete from system")
#     user_id = input("Choose: ")
#     name = module.del_user(user_id)
#     print("User {} is deleted from system".format(name))
#     logger("User {} is deleted from system".format(name))
#     view.admin()

def del_staff():
    print("Choose who you want to fire: ")
    view.show_users()
    new_staff = ""
    user = input("Choose: ")
    name = module.del_staff(user)
    print("{} is deleted from staff".format(name))
    logger(": User {} deleted to staff by admin".format(name))
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

    module.add_product(product_name ,product_price)
    logger(": Product {} add by {} with price by {}".format(product_price, product_name, user_name))
    view.employee()


# def del_product():
#     pr = module.string_from_products().replace("\n"," ")
#     pr1 = pr.split()
#     view.show_pricelist()
#     del_pr = input("Choose what product are you want to delete(Please input the word): ")
#
#     for i in range(0, len(pr1)):
#         if del_pr == pr1[i]:
#             pr = pr.replace((pr1[i-1] + " " + pr1[i]+" "+ pr1[i+1]),"")
#     pr = pr.split(" ")
#     if "" in pr:
#         del pr[pr.index("")]
#
#     id = []
#     prod = []
#     price = []
#     for i in range(0, len(pr), 3):
#         id.append(pr[i])
#     for i in range(1, len(pr), 3):
#         prod.append(pr[i])
#     for i in range(2, len(pr), 3):
#         price.append(pr[i])
#
#     if "" in id:
#         del id[id.index("")]
#
#     for i in range(1, len(id)):
#         if int(id[i-1]) + 1 == int(id[i]):
#             pass
#         else:
#             id[i] = str(int(id[i-1]) + 1)
#
#     if "" in id:
#         del id[id.index("")]
#
#     if "" in prod:
#         del prod[prod.index("")]
#
#     if "" in price:
#         del price[price.index("")]
#
#     res = ""
#
#     for i in range(0, len(price)):
#         res += id[i] + " " + prod[i] + " " + price[i] + "\n"
#
#     module.update_products(res)
#     logger("{} is deleted from products".format(del_pr))
#     view.employee()


def change_prices():

    # products1 = print_all_products()
    # products = []
    #
    # for i in range(4, len(products1), 3):
    #     products.append(products1[i])
    # print(products)

    print("Select the product for which you want to change a price")
    view.show_pricelist()
    product = input("Select(Name of product)): ")
    new_price = input("Add the new price: ")
    old_price = ""
    old_price = module.change_price(product, new_price)

    # # print(products)
    # for i in range(0, len(products)):
    #     if new_price.isdigit():
    #
    #         if int(answer) - 1 == i:
    #
    #             a = print_all_products()
    #             n = answer
    #             p = new_price
    #
    #             # for i in range(5,len(a),3):
    #             for i in range(0, len(a)):
    #                 if n == a[i]:
    #                     old_price = a[i+2]
    #                     a[i + 2] = p
    #                     prod = a[i+1]
    #
    #             res = a[0] +" "
    #
    #             for i in range(1, len(a)):
    #                 res += a[i] +" "
    #
    #
    #             res = res.split(" ")
    #             if "" in res:
    #                 del res[res.index("")]
    #             if "" in res:
    #                 del res[res.index("")]
    #
    #
    #             id = []
    #             product = []
    #             price = []
    #             for i in range(0, len(res), 3):
    #                 id.append(res[i])
    #
    #             for i in range(1, len(res), 3):
    #                 product.append(res[i])
    #
    #             for i in range(2, len(res), 3):
    #                 price.append(res[i])
    #
    #             res = ""
    #             for i in range(0 , len(product)):
    #                 res += id[i]+" " + product[i] + " " + price[i] + "\n"
    #             module.change_price(res)
    #             print("The price is changed")
    #     else:
    #         print("Error.Try again")
    #         change_prices()
    logger(": {} is changed {} price from {} to {}".format(user_name, product,old_price, new_price))
    view.employee()

def logger(operation):
    date1 = datetime.datetime.now()
    res = ""
    date_now = str(date1.day) + "-" + str(date1.month) + "-" + str(date1.year) + "/" + str(date1.hour) + ":" + str(date1.minute)
    res += date_now + "." + user_name + "." + operation
    module.add_log(res)

def reg():
    user_name = input("Please, input the login: ")
    user_password = input("Please, input the password: ")
    logger(": New account {}".format(user_name))
    module.reg(user_name,user_password)
    view.welcome()

def log_in():
    global user_name
    user_name = input("Login: ")
    user_password = input("Password: ")

    role = module.login(user_name, user_password)
    role = role[0]

    if role == "admin":
        print(f"Hello admin {user_name}")
        logger(": Admins session start")
        view.admin()
    elif role == "staff":
        print(f"Hello employee {user_name}")
        logger(": Staffs session start")
        view.employee()
    elif role == "client":
        print(f"Hello client {user_name}")
        logger(": Clients session start")
        view.client()




def list_all_users():
    us =  module.string_from_users()
    us = us.replace("\n"," ")
    s = us.split(" ")
    users = []
    for i in range(6, len(s), 5):
            users.append(s[i])
    return users