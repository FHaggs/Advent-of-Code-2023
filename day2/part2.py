import re


def calc_game(line):
    
    result_list = []

    match = re.search(r'Game (\d+):', line)
    game_num = match.group(1)

    after_colon = line.split(":", 1)[1].strip()
    

    games = after_colon.split(';')
    
    for game in games:
        matches = re.findall(r'(\d+)\s*(\w+)', game)
        color_dict = {color: int(quantity) for quantity, color in matches}
        result_list.append(color_dict)
        # Define color thresholds
    final_dict = {"blue": 0, "red": 0, "green":0}
    for result in result_list:
        for color, value in result.items():
            if final_dict[color] < value:
                final_dict[color] = value

    res = 1
    for value in final_dict.values():
        res = res * value

    return res
    # Print the result
sum = 0

with open('input_2.txt') as my_file:
    for line in my_file:
        sum += calc_game(line)
print(sum)

#print(calc_game("Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue"))


