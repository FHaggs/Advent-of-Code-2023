values = []
nums = {"zero": 0, "one": 1, "two": 2, "three": 3, "four": 4, "five": 5,
        "six": 6, "seven": 7, "eight": 8, "nine": 9}


def get_value(line):

    first_num = None
    last_num = None
    

    for word, num in nums.items():
        replaced = word[0] + str(num) + word[-1]
        line = line.replace(word, replaced)

#    print(line)
    for i in range(len(line)):

        if line[i].isdigit():
            last_num = int(line[i])
            if first_num is None:
                first_num = int(line[i])

    finalnum = first_num * 10 + last_num
    return finalnum


with open('testedata1.txt') as my_file:
    for line in my_file:
        values.append(get_value(line))

sum = 0

for val in values:
    sum += val

# numteste = get_value("eighthree")
print(sum)
