#   Question: 36. Valid Sudoku
# Difficulty: Easy
#       Tags: Hash Table
'''
Determine if a Sudoku is valid, according to: Sudoku Puzzles - The Rules.
The Sudoku board could be partially filled, where empty cells are filled with the character '.'.

Note:
A valid Sudoku board (partially filled) is not necessarily solvable. Only the filled cells need to be validated.
'''
from collections import Counter


def check_one_list(nums):
    result = True
    h = Counter(nums)
    for k, v in h.items():
        if k != ".":
            if int(k) > 9 or int(k) < 1 or v > 1:
                result = False
                break
    return result


def check_lists(lists):
    result = True
    for i in range(len(lists)):
        if check_one_list(lists[i]) == False:
            result = False
            break
    return result


def build_blocks(board):
    block_list = []
    blocks = []
    one = []
    for i in range(0, len(board), 3):
        one += list(zip(board[i], board[i + 1], board[i + 2]))
    block_list += [one[m: m + 3] for m in range(0, len(one), 3)]
    for block in block_list:
        blocks.append([i for sub in block for i in sub])
    return blocks


class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        result = False
        if check_lists(board) == True:
            if check_lists(list(zip(*board))) == True:
                if check_lists(build_blocks(board)) == True:
                    result = True

        return result