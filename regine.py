import time
from colorama import Fore, Style

def pozitie_corecta_tabla(testRow, testCol, solutie_curenta):
    if testRow == 0:
        return True

    for row in range(0, testRow):
        if testCol == solutie_curenta[row] or abs(testRow - row) == abs(testCol - solutie_curenta[row]):
            return False

    return True

def pozitionare_solutii(row, numar_regine, solutie_curenta, solutii):
    for col in range(numar_regine):
        if not pozitie_corecta_tabla(row, col, solutie_curenta):
            continue
        else:
            solutie_curenta[row] = col
            if row == (numar_regine - 1):
                solutii.append(solutie_curenta.copy())
            else:
                pozitionare_solutii(row + 1, numar_regine, solutie_curenta, solutii)

def gaseste_solutii(numar_regine):
    solutii = []
    solutie_curenta = [0 for x in range(numar_regine)]
    pozitionare_solutii(0, numar_regine, solutie_curenta, solutii)
    return solutii

def afisare(solution):
    print("+---" * len(solution) + "+")
    for row in range(len(solution)):
        line = "|"
        for col in range(len(solution)):
            if col == solution[row]:
                line += f" {Fore.RED}♛{Style.RESET_ALL} |"
            else:
                line += " . |"
        print(line)
        print("+---" * len(solution) + "+")

def vizualizare(solutii):
    for idx, solutie in enumerate(solutii):
        print(f"{Fore.GREEN}Solutia numarul: {idx + 1}{Style.RESET_ALL}")
        afisare(solutie)
        print("\n")

def salvare_in_fisier(solutii, nume_fisier):
    with open(nume_fisier, 'a', encoding='utf-8') as file:
        for idx, solutie in enumerate(solutii):
            file.write(f"Solutia numarul: {idx + 1}\n")
            for row in range(len(solutie)):
                line = ""
                for col in range(len(solutie)):
                    if col == solutie[row]:
                        line += " ♛ "
                    else:
                        line += " . "
                file.write(line + "\n")
            file.write("\n")


numar_regine = 8
print("Gasirea solutiilor pentru " + str(numar_regine) + " Regine ")
time.sleep(2)
solutii = gaseste_solutii(numar_regine)
print(len(solutii), "solutions found")

vizualizare(solutii)

optiune_salvare = input("Doriți să salvați soluțiile într-un fișier? (da/nu): ")
if optiune_salvare.lower() == "da":
    nume_fisier = input("Introduceți numele fișierului de salvare (ex. solutii.txt): ")
    salvare_in_fisier(solutii, nume_fisier)
    print(f"Solutiile au fost salvate in fisierul {nume_fisier}.")
else:
    print("Programul se încheie.")
