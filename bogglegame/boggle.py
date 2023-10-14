"""
File: boggle.py
Name: Sunny
----------------------------------------
While user enter four row of alphabet(contains 4 alphabet with three space),
this program will loop over every nearby alphabet and check if there are
vocabulary that exist in dictionary.txt. It will print founded word and
calculate how many words been found.
"""

import time

# This is the file name of the dictionary txt file
# we will be checking if a word exists by searching through it
FILE = 'dictionary.txt'


def main():
    """
    This part first read the dict.txt file, make a boggle board,
    check every single alphabet, and do the recursion.
    """
    start = time.time()
    ####################
    ans_lst = []
    dictionary = read_dictionary()
    boggle_list = make_board()
    if len(boggle_list) == 4:
        for i in range(len(boggle_list)):
            for j in range(len(boggle_list)):
                word = boggle_list[i][j]
                find_word(boggle_list, word, i, j, [[i, j]], ans_lst)
        print('There are ' + str(len(ans_lst)) + ' words in total.')
        ####################
        end = time.time()
        print('----------------------------------')
        print(f'The speed of your boggle algorithm: {end - start} seconds.')


def make_board():
    board = []
    for i in range(4):
        enter = input(str(i + 1) + ' row of letters: ')
        if len(enter) != 7:
            print('Illegal input')
            break
        else:
            line = []
            for j in range(len(enter)):
                if enter[j].isalpha():
                    line += enter[j].lower()
            board.append(line)
    return board


def find_word(boggle_list, current_ans, x, y, used_list, ans_lst, dictionary):
    if current_ans in dictionary and current_ans not in ans_lst:
        if len(current_ans) > 3:
            print('Found "' + current_ans + '"')
            ans_lst.append(current_ans)

    if has_prefix(current_ans, dictionary):  # Start to check vocab by 3*3
        for i in range(-1, 2):
            for j in range(-1, 2):
                neighbor_x = x + j
                neighbor_y = y + i
                print(neighbor_x, neighbor_y)
                if 0 <= neighbor_x < len(boggle_list) and 0 <= neighbor_y < len(boggle_list) and (neighbor_x, neighbor_y) not in boggle_list:

                    # Choose
                    if [neighbor_x, neighbor_y] not in used_list:
                        current_ans += boggle_list[neighbor_x][neighbor_y]
                        used_list.append([neighbor_x, neighbor_y])

                        # Explore
                        find_word(boggle_list, current_ans, neighbor_x, neighbor_y, used_list, ans_lst, dictionary)

                        # Un-choose
                        current_ans = current_ans[:len(current_ans)-1]
                        used_list.pop()


def read_dictionary():
    """
    This function reads file "dictionary.txt" stored in FILE
    and appends words in each line into a Python list
    """
    python_lst = []
    with open(FILE, 'r') as f:
        for line in f:
            python_lst.append(line.strip())
    return python_lst


def has_prefix(sub_s, dictionary):
    """
    :param sub_s: (str) A substring that is constructed by neighboring letters on a 4x4 square grid
    :return: (bool) If there is any words with prefix stored in sub_s
    """
    for word in dictionary:
        if word.startswith(sub_s):
            return True
    return False


if __name__ == '__main__':
    main()
