from pythonShop import control,view

def add_log(res):
    f = open("data/log","a")
    res += "\n"
    f.write(res)
    f.close()

def reg(user_name,user_password):
    st_users = string_from_users()
    if len(st_users) == 0:
        f = open('data/users','w')
        f.write("0 login password cash role")
        f.write("\n")
        f.close()

    st_users =  st_users.replace("\n"," ")
    ls_users = st_users.split(" ")
    if "" in ls_users:
        del ls_users[ls_users.index("")]
    #print(ls_users)
    if len(st_users) > 0:
        id = int( ls_users[len(ls_users) - 5])
    else:
        id = 0

    id += 1

    role = "client"
    if user_name not in ls_users:
        with open('data/users','a') as f:
            if id == 1:
                role = "admin"
            f.write(str(id)+" "+f"{user_name}" +" "+f"{user_password}"+" "+"100" + " " +f"{role}")
            f.write("\n")
    else:
        print("This person already registred")
    view.welcome()


def ls_clients():
    us = string_from_users().replace("\n"," ")
    us = us.split(" ")
    #print(us)
    rez = ""
    res = []
    fin = ""
    for i in range (0, len(us)):
        if us[i] == "client":
            rez += us[i-4]+" "+(us[i-3]) +" "+ us[i-1]
            res.append(rez)
            rez = ""
    for i in res:
        fin += i + " "
    return fin





def string_from_users():
    f = open('data/users')
    us = ""
    while True:
        users = f.readline()
        if len(users) == 0:
            break
        us += users

    f.close()
    return us

def add_product(product_name ,product_price):
    str_products = string_from_products().replace("\n", " ")
    ls_products = control.print_all_products()
    f = open("data/products", 'a')

    if len(str_products) == 0:
        f.write("0 product price")
        f.write("\n")
        f.close()

    f = open('data/products', 'a')
    str_products1 = string_from_products().replace("\n", " ")

    pr = str_products1.split(" ")
    if "" in pr:
        del pr[pr.index("")]

    #print(pr)
    id = int(pr[len(pr) - 3])
    id += 1

    if product_name not in ls_products:
        f.write(str(id) + " " + product_name + " " + product_price)
        f.write("\n")
    else:
        print("This product is already in the list")

    f.close()
    print("Do you want to add more products?")
    a = input("Y/N: ")
    if a.lower() == "y":
       control.add_product()
    else:
        view.employee()

def update_users(res):
    f2 = open("data/users", "w")
    f2.write(res)
    f2.close()

def update_history(check):
    f1 = open("data/history", "a")
    f1.write(check)
    f1.close()

def string_from_history():
    f = open("data/history")
    hs = ""
    while True:
        history = f.readline()
        if len(history) == 0:
            break
        hs += history

    f.close()
    return hs


def string_from_products():
    f = open('data/products')
    pr = ""
    while True:
        products = f.readline()
        if len(products) == 0:
            break
        pr += products

    f.close()
    return pr

def update_products(res):
    f = open("data/products","w")
    f.write(res)
    f.close()


def add_staff(res):
    id = []
    login = []
    password = []
    cash = []
    role = []
    for i in range(0, len(res),5):
        id.append(res[i])
    for i in range(1, len(res),5):
        login.append(res[i])
    for i in range(2, len(res),5):
        password.append(res[i])
    for i in range(3, len(res),5):
        cash.append(res[i])
    for i in range(4, len(res),5):
        role.append(res[i])

    rez = ""
    for i in range(0, len(role)):
        rez += id[i]+" " + login[i]+" "+password[i]+" "+cash[i]+" "+role[i] + "\n"

    f = open("data/users","w")
    f.write(rez)
    f.close()

def change_price(res):
    f = open('data/products', 'w')
    f.write(res)

    f.close()