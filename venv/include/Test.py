def string_from_clients():
    f = open('clients')
    cl = ""
    while True:
        clients = f.readline()
        if len(clients) == 0:
            break
        cl += clients

    f.close()
    return cl


a = string_from_clients()
print(a)
b = string_from_clients()
print(b)