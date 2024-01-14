import time
from colorama import Fore, Style

def pozitie_corecta_tabla(testRow, testCol, solutie_curenta):
    return testRow == 0 or all(
        testCol != solutie_curenta[row] and abs(testRow - row) != abs(testCol - solutie_curenta[row])
        for row in range(testRow)
    )

def pozitionare_solutii(row, numar_regine, solutie_curenta, solutii):
    for col in range(numar_regine):
        if pozitie_corecta_tabla(row, col, solutie_curenta):
            solutie_curenta[row] = col
            if row == numar_regine - 1:
                solutii.append(solutie_curenta[:])
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
        return "Eroare: Numele fișierului trebuie să aibă extensia .txt."

    try:
        with open(nume_fisier, "w", encoding="utf-8") as file:
            for idx, solutie in enumerate(solutii):
                file.write(f"Solutia numarul: {idx + 1}\n")
                file.write(tabla_to_str(solutie))
                file.write("\n")
        return f"Fișierul {nume_fisier} a fost creat cu succes!"
    except Exception as e:
        return f"Eroare la crearea fișierului: {e}"



def tabla_to_str(tabla):
    result = ""
    for row in tabla:
        line = "|"
        for col in range(len(tabla)):
            line += f" {'♛' if col == row else '.'} |"
        result += line + "\n" + "+---" * len(tabla) + "+\n"
    return result

def get_validare_numar_regine():
    while True:
        try:
            numar_regine = int(input("Introduceți numărul de regine (între 4 și 10): "))
            if 4 <= numar_regine <= 10:
                return numar_regine
            else:
                raise ValueError("Numărul de regine trebuie să fie între 4 și 10.")
        except ValueError as e:
            print(f"Erroare: {e}")
            retry = input("Doriți să încercați din nou? (da/nu): ").lower()
            if retry != 'da':
                raise

def get_validare_da_nu():
    while True:
        raspuns = input("Doriți să salvați soluțiile într-un fișier? (da/nu): ").lower()
        if raspuns.strip() in ['da', 'nu']:
            return raspuns.strip()
        else:
            print("Eroare: Răspunsul trebuie să fie 'da' sau 'nu'.")

def main():
    numar_regine = get_validare_numar_regine()
    solutii = gaseste_solutii(numar_regine)
    print(len(solutii), "solutions found")

    vizualizare(solutii)

    salvare = get_validare_da_nu()
    if salvare == "da":
        while True:
            nume_fisier = input("Introduceți numele fișierului de salvare (implicit: solutii_regine.txt): ")
            if not nume_fisier:
                nume_fisier = "solutii_regine.txt"
                break
            elif not nume_fisier.lower().endswith(".txt"):
                print("Eroare: Numele fișierului trebuie să aibă extensia .txt.")
                continue
            else:
                break
        rezultat_salvare = salvare_in_fisier(solutii, nume_fisier)
        print(rezultat_salvare)

if __name__ == "__main__":
    main()
