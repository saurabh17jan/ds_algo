

def remove_same_char_from_mid(line):
    """
    This method will remove the same chracters if present in the middle of the line
    :param line: Give any String
    :return: it will return the length of last string whose mid characters are not same
    """
    if len(line) == 0:
        """
        this handles 2 special conditions
            1. What if there is no input
            2. it also handles the scenario where same chars like 'cccc' are passed which will eventually get removed to '' empty_input_string
        """
        print(0)
        return

    if len(line) == 1:
        """this condition came up even all the character of 1 side started matching to the Remove_character from mid position
           eg: "baaa" or "aaab"
        """
        print(1)
        return

    """
    Now if the String len(line) > 1, then proceed with following
    Slicing the given string into 2 halves
    """
    l = len(line)
    ini_first__half = line[:int(l / 2)]
    ini_second_half = line[int(l / 2):]

    """
    initialize the left and right indexes from the mid positions
    """
    left_max_idx = len(ini_first__half) - 1
    right_min_idx = len(ini_first__half)

    if ini_first__half[left_max_idx] == line[right_min_idx]:
        """
        Check if the mid characters are same, and if they are then proceed with string reduction phase
        """
        flag = True
        char_to_be_removed = ini_first__half[left_max_idx]   # identify which char to be removed

        """
        slide index position appropriately
        """
        left_max_idx = left_max_idx - 1
        right_min_idx = right_min_idx + 1

        """
        added the index position check to make sure they(both index position) do not go beyond the length of string in either direction 
        -- in scenarios where all characters in the input are same
        """
        while flag: # and right_min_idx < len(line) and left_max_idx > -1 :
            if right_min_idx < len(line):
                """ kept this condition outside so that line[right_min_idx] do not go out of index even while comparing"""
                if line[right_min_idx] == char_to_be_removed:
                    right_min_idx= right_min_idx +1
                    right_flg = True
                else:
                    right_flg = False
            else:
                right_flg = False

            if left_max_idx > -1:
                """ kept this condition outside so that line[left_max_idx] do not go out of index even while comparing"""
                if line[left_max_idx] == char_to_be_removed:
                    left_max_idx  = left_max_idx  - 1
                    left_flg = True
                else:
                    left_flg = False
            else:
                left_flg = False

            if right_flg or left_flg:
                """keep doing it untill all the character which needs to be skipped are covered off by the indes position ineither direction"""
                flag = True
            else:
                flag = False

        # print(line[:left_max_idx+1] + line[right_min_idx:])
        # if len(line[:left_max_idx+1]):
        remove_same_char_from_mid(line[:left_max_idx+1] + line[right_min_idx:])
    else:
        print(len(ini_second_half+ini_first__half))


if __name__ == '__main__':
"""
 Author: @saurabh17jan
 Date:   2020-08-11
"""
    # print("Hello World")
    # aabcccabba
    # aabcc
    # cabba
    # line = "aabcccabba"  #4
    # line = "aabcccabbad" # 11
    # line = "daabcccabbad" #4
    # line = "aabccccbba"  #0
    # line = "cccc" #0
    # line = "abccba" #0
    #line = "abaa" #1
    #line = "aaba" #1
    line = "aabaaa" #1

    if len(line) > 2:

        ini_first__half = line[:int(len(line)/ 2)]
        ini_second_half = line[int(len(line)/ 2):]
        # for reverse new_set ini_second_half+ini_first__half
        reverse_line = ini_second_half + ini_first__half
        print(reverse_line)
        remove_same_char_from_mid(reverse_line)

