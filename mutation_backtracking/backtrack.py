# backtracking_problems.py

def is_valid_sudoku(board):
    def is_valid_row(row):
        seen = set()
        for num in board[row]:
            if num != '.':
                if num in seen:
                    return False
                seen.add(num)
        return True

    def is_valid_column(col):
        seen = set()
        for row in range(9):
            num = board[row][col]
            if num != '.':
                if num in seen:
                    return False
                seen.add(num)
        return True

    def is_valid_box(row, col):
        seen = set()
        for i in range(row, row + 3):
            for j in range(col, col + 3):
                num = board[i][j]
                if num != '.':
                    if num in seen:
                        return False
                    seen.add(num)
        return True

    for i in range(9):
        if not is_valid_row(i) or not is_valid_column(i):
            return False

    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            if not is_valid_box(i, j):
                return False

    return True

def solve_sudoku(board):
    def is_valid(row, col, num):
        for i in range(9):
            if board[row][i] == num or board[i][col] == num or board[3 * (row // 3) + i // 3][3 * (col // 3) + i % 3] == num:
                return False
        return True

    def solve():
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    for num in map(str, range(1, 10)):
                        if is_valid(i, j, num):
                            board[i][j] = num
                            if solve():
                                return True
                            board[i][j] = '.'
                    return False
        return True

    solve()

def letter_combinations(digits):
    if not digits:
        return []

    mapping = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno',
               '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}

    def backtrack(index, path):
        if index == len(digits):
            combinations.append(path)
            return

        for char in mapping[digits[index]]:
            backtrack(index + 1, path + char)

    combinations = []
    backtrack(0, '')
    return combinations

def generate_parentheses(n):
    def backtrack(s='', left=0, right=0):
        if len(s) == 2 * n:
            combinations.append(s)
            return

        if left < n:
            backtrack(s + '(', left + 1, right)
        if right < left:
            backtrack(s + ')', left, right + 1)

    combinations = []
    backtrack()
    return combinations

def exist(board, word):
    def backtrack(i, j, k):
        if not (0 <= i < len(board)) or not (0 <= j < len(board[0])) or board[i][j] != word[k]:
            return False

        if k == len(word) - 1:
            return True

        tmp, board[i][j] = board[i][j], '/'
        res = backtrack(i + 1, j, k + 1) or backtrack(i - 1, j, k + 1) or backtrack(i, j + 1, k + 1) or backtrack(i, j - 1, k + 1)
        board[i][j] = tmp
        return res

    for i in range(len(board)):
        for j in range(len(board[0])):
            if backtrack(i, j, 0):
                return True

    return False

def combination_sum(candidates, target):
    def backtrack(start, target, path):
        if target == 0:
            combinations.append(path)
            return

        for i in range(start, len(candidates)):
            if candidates[i] > target:
                continue
            backtrack(i, target - candidates[i], path + [candidates[i]])

    combinations = []
    candidates.sort()
    backtrack(0, target, [])
    return combinations

def sudoku_solver(board):
    def is_valid(row, col, num):
        for i in range(9):
            if board[row][i] == num or board[i][col] == num or board[3 * (row // 3) + i // 3][3 * (col // 3) + i % 3] == num:
                return False
        return True

    def solve():
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    for num in map(str, range(1, 10)):
                        if is_valid(i, j, num):
                            board[i][j] = num
                            if solve():
                                return True
                            board[i][j] = '.'
                    return False
        return True

    solve()


