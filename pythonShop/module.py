from pythonShop import control,view
import pymysql
from random import randint
import time
global db
global sql

db = pymysql.connect(  db = "MyShop",
                       user = 'root',
                       password = '12345678910',
                       host = 'localhost')
sql = db.cursor()


def add_log(res):
    #print(res)
    res = res.split(".")

    sql.execute(f"INSERT INTO log VALUES('{str(res[0])}','{str(res[1])}','{str(res[2])}')")
    #sql.execute(f"INSERT INTO users VALUES({0},'{user_name}', '{user_password}', {100},'{role}')")
    db.commit()

    # f = open("data/log","a")
    # res += "\n"
    # f.write(res)
    # f.close()


def get_check():
    name = control.get_user_name()
    sql.execute(f"SELECT date,product,money_left FROM history WHERE user_name='{name}'")
    check = sql.fetchall()
    return check
def login(user_name,user_password):
    sql.execute(f'SELECT user_name FROM users WHERE user_name="{user_name}"')
    if sql.fetchone() is None:
        print("You are not registered")
        answer = input("Do you want to register? Y/N: ")
        if answer == 'Y' or answer == 'y':
            control.reg()
        else:
            print("Ok")
            view.welcome()
    else:
        sql.execute(f"SELECT user_name FROM users WHERE user_password = '{user_password}'")
        a = sql.fetchall()
        user_l = tuple([user_name])

        if a is None:
            print("Not correct!!")
        else:

            if (user_l) not in a:
                print("Not correct")
            else:
                sql.execute(f"SELECT role FROM users WHERE user_name = '{user_name}'")
                role = sql.fetchone()
                return role


def list_users():
    sql.execute(f"SELECT id,user_name,role FROM users")
    ls_us = sql.fetchall()
    return ls_us


def reg(user_name,user_password):
    role = "client"


    sql.execute(f"SELECT user_name FROM users WHERE user_name = '{user_name}'")
    if sql.fetchone() is None:

        sql.execute(f"INSERT INTO users VALUES({0},'{user_name}', '{user_password}', {100},'{role}')")
        db.commit()
        sql.execute(f"SELECT id FROM users WHERE user_name = '{user_name}'")
        id1 = sql.fetchone()

        if id1[0] == 1:
            role = "admin"
            sql.execute(f"UPDATE users SET role = '{role}' WHERE id = 1")
            db.commit()

        print("Registration complete!")
    else:
        print("Error. You are already registered.")
        control.reg()


def add_staff(id):
    new_staff = ""
    sql.execute(f"SELECT role FROM users WHERE id = '{id}'")
    role = sql.fetchone()
    if role[0] == "client":
        role = 'staff'
        sql.execute(f"UPDATE users SET role='{role}' WHERE id = '{id}'")
        db.commit()
        sql.execute(f"SELECT user_name FROM users WHERE id = '{id}'")
        new_staff = sql.fetchone()
    else:
        print("This person is already in staff")
        control.add_staff()
    return new_staff[0]



# def del_user(id):
#     sql.execute(f"SELECT user_name FROM users WHERE id = '{id}'")
#     name = sql.fetchone()
#     sql.execute(f"DELETE FROM users WHERE id = '{id}'")
#     db.commit()
#     sql.execute(f"SELECT id FROM users")
#     id_list = sql.fetchall()
#     print(id_list)
#
#     return name[0]

def del_staff(id):
    new_staff = ""
    sql.execute(f"SELECT role FROM users WHERE id = '{id}'")
    role = sql.fetchone()
    if role[0] == "staff":
        role = 'client'
        sql.execute(f"UPDATE users SET role='{role}' WHERE id = '{id}'")
        db.commit()
        sql.execute(f"SELECT user_name FROM users WHERE id = '{id}'")
        new_staff = sql.fetchone()
    else:
        print("This person is not in staff")
        control.add_staff()
    return new_staff[0]




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

def show_pricelist():
    sql.execute(f"SELECT * FROM products")
    price_list = sql.fetchall()

    res = ''
    if price_list is None:
        pass
    else:
        for i in range(0,len(price_list)):
           res += "ID: " + str(price_list[i][0]) + ", Product: " + str(price_list[i][1]) + ", Price: " + str(price_list[i][2]) +"\n"

    return res


def add_product(product_name ,product_price):
    sql.execute(f"SELECT product FROM products WHERE product='{product_name}'")
    if sql.fetchone() is None:
        sql.execute(f"SELECT product FROM products")
        s =sql.fetchall()
        if product_name not in s:
            sql.execute(f"INSERT INTO products VALUES({0}, '{product_name}','{product_price}')")
            db.commit()
    else:
        print("This product already in shop")
        control.add_product()

    # str_products = string_from_products().replace("\n", " ")
    # ls_products = control.print_all_products()
    # f = open("data/products", 'a')
    #
    # if len(str_products) == 0:
    #     f.write("0 product price")
    #     f.write("\n")
    #     f.close()
    #
    # f = open('data/products', 'a')
    # str_products1 = string_from_products().replace("\n", " ")
    #
    # pr = str_products1.split(" ")
    # if "" in pr:
    #     del pr[pr.index("")]
    #
    # #print(pr)
    # id = int(pr[len(pr) - 3])
    # id += 1
    #
    # if product_name not in ls_products:
    #     f.write(str(id) + " " + product_name + " " + product_price)
    #     f.write("\n")
    # else:
    #     print("This product is already in the list")
    #
    # f.close()
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

def shop(cash_before_buy, price, name):
    cash_left = int(cash_before_buy) - int(price)
    sql.execute(f"UPDATE users SET cash={cash_left} WHERE user_name='{name}'")
    db.commit()
def add_history(check):
    name = control.get_user_name()
    check = check.split(" ")
    print(check)
    sql.execute(f"INSERT INTO history VALUES('{check[0]}','{check[1]}',{check[2]},'{name}')")
    db.commit()

def deal_with_devil(name):
    sql.execute(f"UPDATE users SET cash=100 WHERE user_name = '{name}'")
    db.commit()

def get_cash(name):
    sql.execute(f"SELECT cash FROM users WHERE user_name='{name}'")
    cash = sql.fetchone()[0]
    return cash

def get_price(product):
    sql.execute(f"SELECT price FROM products WHERE product = '{product}'")
    price = sql.fetchone()[0]
    return price


def change_price(product, new_price):
    old_price = ""
    sql.execute(f"SELECT product FROM products")
    pr = sql.fetchall()

    product1 = tuple([product])

    if product1 in pr:
        sql.execute(f"SELECT price FROM products WHERE product = '{product}'")
        old_price = sql.fetchone()[0]
        sql.execute(f"UPDATE products SET price='{new_price}' WHERE product = '{product}'")
        db.commit()
        return old_price
    else:
        print("Error product")
        control.change_prices()
