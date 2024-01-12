import time

numar_regine = 8
solutie_curenta = [0 for x in range(numar_regine)]
solutii = []

def pozitie_corecta_tabla(testRow, testCol):
    if testRow == 0:
        return True

    for row in range(0, testRow):
        if testCol == solutie_curenta[row] or abs(testRow - row) == abs(testCol - solutie_curenta[row]):
            return False

    return True

def pozitionare_solutii(row):
    global solutie_curenta, solutii, numar_regine

    for col in range(numar_regine):
        if not pozitie_corecta_tabla(row, col):
            continue
        else:
            solutie_curenta[row] = col
            if row == (numar_regine - 1):
                solutii.append(solutie_curenta.copy())
                print("Solution number", len(solutii), solutie_curenta)
            else:
                pozitionare_solutii(row + 1)


time.sleep(2)
pozitionare_solutii(0)

for solutie in solutii:
    print(solutie)
