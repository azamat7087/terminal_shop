a = "0 product price 1 as 12 2 Snickers 13"
a = a.split(" ")
n = input("N: ")
p = input("P: ")
# for i in range(5,len(a),3):
for i in range(0,len(a)):
    if n == a[i]:
        a[i+2] = p

res = a[0]

for i in range(1,len(a)):
    res += " " + a[i]

print( res)