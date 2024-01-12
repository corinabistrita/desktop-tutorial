""""
variabile: nr de regina=
var pt stocarea solutie curente si gasite 

fc pozitionare regina (rand):
        
        for coloana in interval(numarRegine):
           nu e singura(rand, coloana):
                continua
            altfel
                solutieCurenta := coloana
                if rand == (numarRegine - 1):
 
                altfel
                    AseazaRegina(rand + 1


   functie pozitie corecta(Rand, Coloana)
        #verificarea randului

#verificare coloana
        for rand  in (0, Rand):
            if coloana == solutia[rand]:
                return fals

            #verificare diagonala
            if |testRand - rand| == |testColoana - solutie[rand]|:
                return Fals

       
        return Adevărat

    fc pozitionarea reg(rand):
        
        if coloana in interval(numarRegine):
            if nu e singura(rand, coloana):
                continua
            altfel:
                solcurenta[rand] := coloana
                if rand == (numarRegine - 1);
                    ...lista de sol gasite..
                    afisarea lor 
			else
                    AseazaRegina(rand + 1)


finalul.."
"""
numar_queens = 8  
solutie_curenta =  
solutions = []

#functia de pozitionarea/verificarea corecta a reginei pe tabla de sah(orizontal,vertical,si diagonal)

def pozitionarea_reginei(board,row,col):
    #orizontal 
    for i in range(col):
        if board[row][i] == 1:
            return 
     #diagonal   
     for i,j in zip(range(row,-1,-1),range(col,-1,-1)):
        if board[i][j] == 1:
        return 
    
    return True


def pozitionare(row):
    global solutie_curenta, solutions, numar_queens

    stack = [(row, 0)] 
    while stack:
        current_row, current_col = stack.pop()

        for col in range(current_col, numar_queens):
            if not pozitionare (current_row, col):
                continue

            currentSolution[current_row] = col

            if current_row == (numar_queens - 1):
            else:
                stack.append((current_row + 1, 0))
                stack.append((current_row, col + 1))
                break


for solution in solutions:
    print(solution)



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
