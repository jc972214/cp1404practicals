for i in range(1, 21, 2):
    print(i, end=' ')
print()

# a.
for i in range(0, 101, 10):
    print(i, end=' ')
print()

# b.
for i in range(20, 0, -1):
    print(i, end=' ')
print()

# c.
number_of_stars = int(input("Enter Number of Stars:"))
for i in range(number_of_stars):
    print('*', end=' ')
print()

# d.
star_layer = 1
for i in range(number_of_stars):
    for x in range(0, star_layer, 1):
        print('*', end=' ')
    print()
    star_layer = star_layer + 1
