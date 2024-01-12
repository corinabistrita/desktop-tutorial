numar_Regine = 8
solutii = []

def afisare_solutie(board):
    for row in board:
        print(row)
    print()

def pozitii_corecte(board, row, col):
    for i in range(row):
        if board[i][col] == 1 or \
           (col - (row - i) >= 0 and board[i][col - (row - i)] == 1) or \
           (col + (row - i) < numar_Regine and board[i][col + (row - i)] == 1):
            return False
    return True

def rezolvare(board, row):
    global numar_Regine, solutii

    if row == numar_Regine:
        solutii.append([r[:] for r in board])
        return

    for col in range(numar_Regine):
        if pozitii_corecte(board, row, col):
            board[row][col] = 1
            rezolvare(board, row + 1)
            board[row][col] = 0

def gaseste_solutii():
    global numar_Regine, solutii

    board = [[0 for _ in range(numar_Regine)] for _ in range(numar_Regine)]
    rezolvare(board, 0)

gaseste_solutii()

print(len(solutii), "solutii gasite")
for solutie in solutii:
    afisare_solutie(solutie)
