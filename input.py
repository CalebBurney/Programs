def create_3d_list_1(x, y, z):
    lst = []
    for i in range(x):
        lst_2d = []
        for j in range(y):
            lst_1d = []
            for k in range(z):
                lst_1d.append('#')
            lst_2d.append(lst_1d)
        lst.append(lst_2d)
    return lst

x = int(input("Enter input: "))
y = int(input("Enter input: "))
z = int(input("Enter input: "))
output_1 = create_3d_list_1(x, y, z)

print(output_1)