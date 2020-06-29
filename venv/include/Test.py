id = ['0', '1', '2', '4', '5']
for i in range(1, len(id), 3):
    if int(id[i - 1]) + 1 == int(id[i]):
        pass
    else:
        id[i] = str(int(id[i - 1]) + 1)