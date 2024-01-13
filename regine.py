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

def salvare_in_fisier(solutii, nume_fisier="solutii_regine.txt"):
    with open(nume_fisier, "w", encoding="utf-8") as file:
        for idx, solutie in enumerate(solutii):
            file.write(f"Solutia numarul: {idx + 1}\n")
            for row in solutie:
                line = "|"
                for col in range(len(solutie)):
                    if col == row:
                        line += f" ♛ |"
                    else:
                        line += " . |"
                file.write(line + "\n")
                file.write("+---" * len(solutie) + "+\n")
            file.write("\n")


def main():
    while True:
        try:
            numar_regine = int(input("Introduceți numărul de regine (între 4 și 10): "))
            if 4 <= numar_regine <= 10:
                break
            else:
                print("Numărul de regine trebuie să fie între 4 și 10. Reîncercați.")
        except ValueError:
            print("Introduceți un număr valid.")

    print(f"Gasirea solutiilor pentru {numar_regine} Regine ")
    time.sleep(2)
    solutii = gaseste_solutii(numar_regine)
    print(len(solutii), "solutions found")

    vizualizare(solutii)

    salvare = input("Doriți să salvați soluțiile într-un fișier? (da/nu): ").lower()
    if salvare == "da":
        nume_fisier = input("Introduceți numele fișierului de salvare (implicit: solutii_regine.txt): ")
        if not nume_fisier:
            nume_fisier = "solutii_regine.txt"
        salvare_in_fisier(solutii, nume_fisier)

if __name__ == "__main__":
    main()
