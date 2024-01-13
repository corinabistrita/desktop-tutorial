# Documentație - Problema Celor 8 Regine pe Tabla de Șah

## Găsirea Soluțiilor pentru Problema Celor 8 Regine

Acest program Python rezolvă problema plasării unui număr variabil de regine (de la 4 la 10 regine) pe o tablă de șah de dimensiune dată, astfel încât să nu existe conflicte între ele. Acesta oferă, de asemenea, opțiuni de afișare în consolă și salvare într-un fișier a soluțiilor găsite.

![queen-solver-animation-6](https://github.com/corinabistrita/desktop-tutorial/assets/88577871/67464f6c-1f5e-4025-aa05-21b3b6f07893)

## Rezolvarea Problemei Celor 8 Regine

Problema celor 8 regine presupune găsirea unei configurații valide așezate pe o tablă de șah 8x8 astfel încât nicio regină să nu amenințe nicio altă regină. Acest program folosește o abordare de tip backtracking și recursivitate pentru a explora toate posibilitățile și a găsi soluții în funcție de numărul de regine introdus de utilizator.

## Regulile Jocului

- **Plasarea Reginelor:**
  - Fiecare regină poate ocupa oricare dintre cele opt coloane ale tablei.
  - Nu pot exista două regine pe aceeași linie sau coloană.
  - O regină amenință orice pătrat de pe aceeași linie, coloană sau diagonală.

- **Scopul Jocului:**
  - Plasarea tuturor celor opt regine pe tablă fără ca acestea să se amenințe reciproc.
  - Soluție pentru cele 8 Regine

## Detalii de Implementare

Programul utilizează o soluție eficientă bazată pe backtracking și recursivitate pentru a explora toate configurațiile posibile și a găsi soluții valide. Algoritmul progresează prin plasarea reginelor pe tablă, verificând continuu dacă configurația curentă respectă regulile jocului.

Pentru a îmbunătăți performanța, se utilizează o optimizare prin faptul că putem plasa o singură regină pe fiecare rând. Astfel, se elimină configurațiile inutile înainte de a avansa la următoarea etapă.

## Utilizare

1. Utilizatorul este solicitat să introducă numărul dorit de regine (între 4 și 10).
2. Programul generează și afișează soluțiile găsite.
3. Utilizatorul decide dacă dorește să salveze soluțiile într-un fișier text, având posibilitatea de a specifica un nume pentru fișier.

Pentru a utiliza acest program, asigurați-vă că aveți instalat modulul `colorama`. Puteți instala acest modul folosind comanda:
```bash
pip install colorama
```