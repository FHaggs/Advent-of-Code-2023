values = []


def get_value(line):

    first_num = None
    last_num = None

    for i in line:
        if i.isdigit():
            last_num = int(i)
            if first_num is None:
                first_num = int(i)

    finalnum = first_num * 10 + last_num
    return finalnum


with open('testedata1.txt') as my_file:
    for line in my_file:
        values.append(get_value(line))

sum = 0

for val in values:
    sum += val

print(sum)
