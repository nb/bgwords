# coding: utf-8
import unittest
import words

class Board:
    def __init__(self, input):
        self.cells = input.strip().split()
        self.width = len(self.cells[0])
        self.height = len(self.cells)

    def inside(self, cell):
        return cell.x >= 0 and cell.x < self.width and cell.y >= 0 and cell.y < self.height

    def at(self, x, y):
        return self.cells[y][x]

    def is_letter(self, cell):
        return self.at(cell.x, cell.y) != '*'

    def __str__(self):
        return '\n'.join(self.cells)
    __repr__ = __str__

class Cell:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __str__(self):
        return 'Cell(%d, %d)' % (self.x, self.y)

    __repr__ = __str__

    def __hash__(self):
        return hash((self.x, self.y))

def next_words(board):
    pass

def paths_from_cell(board, start_cell):
    stack = [{'cell': start_cell, 'path': [], 'visited': set()}]
    while stack:
        args = stack.pop()
        cell = args['cell']
        new_path = args['path'] + [cell]
        new_visited = args['visited'].union([cell])
        yield new_path
        for neighbor in letter_neighbors(board, cell):
             if not neighbor in new_visited:
                 stack.append({'cell': neighbor, 'path': new_path, 'visited': new_visited})

def letters_for_cell(board, cell, all_words):
    for neighbor in letter_neighbors(board, cell):
        for path in paths_from_cell(board, neighbor):
            prefix = string_from_path(board, path)
            for letter in words.alphabet:
                if (prefix + letter) in all_words:
                    yield (letter, prefix + letter, path)

def letters_for_board(board, all_words):
    for x in range(board.width):
        for y in range(board.height):
            if not board.is_letter(Cell(x, y)) and len(list(letter_neighbors(board, Cell(x, y)))) != 0:
                for letter in letters_for_cell(board, Cell(x, y), all_words):
                    yield letter

def string_from_path(board, path):
    return ''.join(reversed([board.at(cell.x, cell.y) for cell in path]))

def neighbors(board, cell):
    for offset in [(-1, 0), (0, 1), (0, -1), (1, 0)]:
        new_cell = Cell(cell.x + offset[0], cell.y + offset[1])
        if board.inside(new_cell):
            yield new_cell

def letter_neighbors(board, cell):
    return (neighbor for neighbor in neighbors(board, cell) if board.is_letter(neighbor))

class Test(unittest.TestCase):
    def test_letter_neighbors(self):
        self.assertEqual([Cell(0, 0), Cell(1, 1), Cell(2, 0)], list(neighbors(self.asterisks(3, 3), Cell(1, 0))))

    def asterisks(self, width, height):
        return Board('\n'.join((['*' * width] * height)))

    def with_letters(self, width, height, letter_cells):
        board = self.asterisks(width, height)
        for cell, letter in letter_cells:
            board.cells[cell.y] = board.cells[cell.y][:cell.x] + letter + board.cells[cell.y][cell.x+1:]
        return board

if __name__ == '__main__':
    big = Board(u"""
*****
*****
*я*н*
пи*а*
онкн*
кораб
сккчи
*зиен
****а
*****
*****
""")
    small = Board(u"""
*1*
23*
**4
""")
    all_words = set(words.read())
    for weee in sorted(letters_for_board(big, all_words), key=lambda x: len(x[1])):
        print weee[0], weee[1], weee[2]
    unittest.main()
