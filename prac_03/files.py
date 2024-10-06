"""File Problems"""


#Q1.

get_name = input("Input your name: ")
out_file = open("name.txt", 'w')
print(get_name, file=out_file)
out_file.close()

#Q2.

in_file = open("name.txt", "r")
name = in_file.read().strip()
in_file.close()
print(f"Hi {name}!")

#Q3.

with open("numbers.txt", "r") as in_file:
    first_number = int(in_file.readline())
    second_number = int(in_file.readline())
    print(first_number + second_number)

#Q4

total_line = 0
with open("numbers.txt", "r") as in_file:
    for line in in_file:
        total_line = int(line) + total_line
    print(total_line)




