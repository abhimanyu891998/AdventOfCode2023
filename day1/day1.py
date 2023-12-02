import re

def part1():
    with open('./input.txt') as input:
        sum = 0
        for line in input.readlines():
            curr_num = 0
            first_digit_idx = re.search('\d', line)
            curr_num = first_digit_idx.group()
            line_r = line[::-1]
            last_digit_idx = re.search('\d', line_r)
            curr_num = curr_num + last_digit_idx.group()
            sum = sum + int(curr_num)

        print(sum)

def part2():
    digit_dict = {
        'zero': '0',
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9'
    }

    digit_dict_r = {
        'orez' : '0',
        'eno' : '1',
        'owt' : '2',
        'eerht' : '3',
        'ruof' : '4',
        'evif' : '5',
        'xis' : '6',
        'neves' : '7',
        'thgie' : '8',
        'enin' : '9'
    }

    with open('./input.txt') as input:
        sum = 0
        s_arr = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        s_arr_r = ['orez', 'eno', 'owt', 'eerht', 'ruof', 'evif', 'xis', 'neves', 'thgie', 'enin', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        for line in input.readlines():
            curr_num = ''
            #search the string in s_arr that occurs the earliest in the line
            first_digit_idx = len(line)
            first_digit = ''
            for s in s_arr:
                if s in line:
                    if line.index(s) < first_digit_idx:
                        first_digit_idx = line.index(s)
                        first_digit = s
            if first_digit in digit_dict:
                curr_num = curr_num + digit_dict[first_digit]
            else:
                curr_num = curr_num + first_digit

            line_r = line[::-1]
            last_digit_idx = len(line_r)
            last_digit = ''
            for s in s_arr_r:
                if s in line_r:
                    if line_r.index(s) < last_digit_idx:
                        last_digit_idx = line_r.index(s)
                        last_digit = s
            if last_digit in digit_dict_r:
                curr_num = curr_num + digit_dict_r[last_digit]
            else:
                curr_num = curr_num + last_digit
            sum = sum + int(curr_num)

        print(sum)



if __name__ == "__main__":
    part1()
    part2()
