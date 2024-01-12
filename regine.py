import time
from colorama import Fore, Style

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
            else:
                pozitionare_solutii(row + 1)

def afisare(solution):
    print("+---" * numar_regine + "+")
    for row in range(numar_regine):
        line = "|"
        for col in range(numar_regine):
            if col == solution[row]:
                line += f" {Fore.RED}♛{Style.RESET_ALL} |"
            else:
                line += " . |"
        print(line)
        print("+---" * numar_regine + "+")

def vizualizare():
    global solutii
    for idx, solutie in enumerate(solutii):
        print(f"{Fore.GREEN}Solutia numarul: {idx + 1}{Style.RESET_ALL}")
        afisare(solutie)
        print("\n")

print("Gasirea solutiilor " + str(numar_regine) + " Regine ")
time.sleep(2)
pozitionare_solutii(0)
print(len(solutii), "solutions found")


vizualizare()
