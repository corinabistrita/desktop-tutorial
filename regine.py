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


