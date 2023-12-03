def get_dict(file_name):
    with open(file_name) as input:
        dict = {}
        for line in input.readlines():
            line = line.strip()
            game_detail, rounds_detail = line.split(':')
            game_num = int(game_detail.strip().split(' ')[1])
            dict[game_num] = {}
            line = rounds_detail.strip()
            rounds = line.split(';')
            for round in rounds:
                round = round.strip()
                round = round.split(',')
                for ball in round:
                    ball = ball.strip()
                    color = ball.split(' ')[1]
                    num = int(ball.split(' ')[0])
                    if color in dict[game_num]:
                        dict[game_num][color].append(num)
                    else:
                        dict[game_num][color] = [num]
            for color in dict[game_num]:
                dict[game_num][color].sort()
        return dict

def part1():
    dict = get_dict('./input.txt')
    red = 12
    blue = 14
    green = 13

    sum_game_num = 0

    for game_num in dict:
        if dict[game_num]['red'][-1] <= red and dict[game_num]['blue'][-1] <= blue and dict[game_num]['green'][-1] <= green:
            sum_game_num = sum_game_num + game_num

    print(sum_game_num)

def part2():
    dict = get_dict('./input.txt')
    sum = 0

    for game_num in dict:
        power = dict[game_num]['red'][-1]*dict[game_num]['blue'][-1]*dict[game_num]['green'][-1]
        sum = sum + power

    print(sum)


if __name__ == "__main__":
    part1()
    part2()