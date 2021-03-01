#!/usr/bin/python3
import sys

def main():
    next_biggest_number(sys.argv[1])


def largest_number(num):
    str_number = str(num)
    str_number_list = [character for character in str_number]
    str_number_list.sort(reverse=True)
    final = int(''.join(str_number_list))
    return final

def increment_sort(num):
    i = -1
    string = str(num)
    lrg_num = largest_number(string)

    for n in [char for char in string]:
        next_val = [character for character in str(lrg_num)][i]
        next_val_i = string.index(next_val)
        sub_largest_num = largest_number(string[next_val_i:])

        sub_num = int(string[next_val_i:])

        if sub_num < sub_largest_num:
            return int(string[:next_val_i] + str(sub_largest_num))
        else:
            i =i - 1
        


def next_biggest_number(num):
    sorted_num = largest_number(num)
    if num == sorted_num:
        return -1
    else:
        return increment_sort(num)

if __name__ == "__main__":
    main()



