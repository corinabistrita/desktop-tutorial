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
                solutii.append([x for x in solutie_curenta])
            else:
                pozitionare_solutii(row + 1, numar_regine, solutie_curenta, solutii)

def gaseste_solutii(numar_regine):
    solutii = []
    solutie_curenta = [0] * numar_regine
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
    if not nume_fisier.lower().endswith(".txt"):
        print("Eroare: Numele fișierului trebuie să aibă extensia .txt.")
        return

    with open(nume_fisier, "w", encoding="utf-8") as file:
        for idx, solutie in enumerate(solutii):
            file.write(f"Solutia numarul: {idx + 1}\n")
            file.write(tabla_to_str(solutie))
            file.write("\n")

    print(f"Fisierul '{nume_fisier}' a fost creat cu succes!")


def tabla_to_str(tabla):
    result = ""
    for row in tabla:
        line = "|"
        for col in range(len(tabla)):
            if col == row:
                line += f" ♛ |"
            else:
                line += " . |"
        result += line + "\n" + "+---" * len(tabla) + "+\n"
    return result

def get_valid_numar_regine():
    try:
        numar_regine = int(input("Introduceți numărul de regine (între 4 și 10): "))
        if 4 <= numar_regine <= 10:
            return numar_regine
        else:
            raise ValueError("Numărul de regine trebuie să fie între 4 și 10.")
    except ValueError as e:
        print(f"Erroare: {e}")
        return get_valid_numar_regine()

def main():
    numar_regine = get_valid_numar_regine()
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
