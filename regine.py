numar_Regine = 8
solutii = []

def pozitii_corecte(board, row, col):
    for i in range(col):
        if board[row][i] == 1:
            return False

    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    
    for i, j in zip(range(row, len(board), 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False #diag,inferioara

    return True

def rezolvare()

    board = [[0 for _ in range(numar_Regine)] for _ in range(numar_Regine)]
    stiva = [(0, 0)] 

    while stiva:
        row, col = stiva.pop()

        while col < numar_Regine:
            if pozitii_corecte(board, row , col):
                board[row][col] = 1
                stiva.append((row, col + 1))  
                break
            else:
                col += 1

        if col == numar_Regine:
            
            if stiva:
                row, _ = stiva.pop()
                col += 1
                board[row][col - 1] = 0  
            else:
                
                break

        if row == numar_Regine - 1 and col == numar_Regine:
           
            solutii.append([row[:] for row in board])

rezolvare()

print(len(solutii), "solutii gasite")
for solutie in solutii:
    print(solutie)
