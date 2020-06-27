a = "0 login 1 aidos 2 Aibol 4 Lane 5 Jack"
a = a.split(" ")
l = []
n = []
res = ''
for i in range(0,len(a),2):
    l.append(a[i])
for i in range(1,len(a),2):
    n.append(a[i])
print(n)

for i in range(1,len(l)):
    if int(l[i-1]) + 1 == int(l[i]):
        pass
    else:
        l[i] = str(int(l[i])-1)

for i in range(0,len(l)):
    res += l[i] + " " + n[i] + " "

print(res)

