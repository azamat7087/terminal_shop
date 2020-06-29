username = "Kate"
st_users ="""0 login password cash role
1 Azamat azamat 100 admin
2 Aibol aibol 100 staff
3 Kate kate 45 client
4 Mike mike 100 client """
cash_after_buy = 12
st_users1 = st_users.replace("\n"," ").split(" ")


for i in range(0, len(st_users1)):
    if username == st_users1[i]:
        st_users1[i+2] = "100"

id = []
login = []
password = []
cash = []
role = []

for i in range(0, len(st_users1),5):
    id.append(st_users1[i])

for i in range(1, len(st_users1),5):
    login.append(st_users1[i])

for i in range(2, len(st_users1),5):
    password.append(st_users1[i])

for i in range(3, len(st_users1),5):
    cash.append(st_users1[i])

for i in range(4, len(st_users1),5):
     role.append(st_users1[i])

res = ""

for i in range (0, len(cash)):
    res+= id[i] +" " +login[i]+" " +password[i] +" "+cash[i]+" "+role[i]+"\n"

print(res)
