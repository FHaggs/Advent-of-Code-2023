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
    color_thresholds = {'red': 12, 'green': 13, 'blue': 14}

    # Check if any dictionary exceeds the color thresholds
    exceeds_threshold = any(
        any(color_dict.get(color, 0) > threshold for color, threshold in color_thresholds.items())
        for color_dict in result_list
    )

    # Print the result
    if exceeds_threshold:
        return 0
    else:
        return int(game_num)
sum = 0

with open('input_2.txt') as my_file:
    for line in my_file:
        sum += calc_game(line)
print(sum)

#print(calc_game("Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue"))


