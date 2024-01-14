# Documentație - Problema Celor 8 Regine pe Tabla de Șah

## Găsirea Soluțiilor pentru Problema Celor 8 Regine

Acest program Python rezolvă problema plasării unui număr variabil de regine (de la 4 la 10 regine) pe o tablă de șah de dimensiune dată, astfel încât să nu existe conflicte între ele. Acesta oferă, de asemenea, opțiuni de afișare în consolă și salvare într-un fișier a soluțiilor găsite sau nu.

## Rezolvarea Problemei Celor 8 Regine

Problema celor 8 regine presupune găsirea unei configurații valide așezate pe o tablă de șah 8x8,dar si nu numai, astfel încât nicio regină să nu amenințe nicio altă regină. Acest program folosește o abordare de tip backtracking și recursivitate pentru a explora toate posibilitățile și a găsi soluții în funcție de numărul de regine introdus de utilizator.

![queen-solver-animation-6](https://coolbutuseless.github.io/img/8queens/anim.gif)

Utilizarea forței brute și încercarea fiecărei combinații posibile de plasare a reginelor pe tablă duce la testarea a 4,426,165,368 de combinații. Dacă putem procesa 50,000 de combinații pe secundă, acest lucru ar dura mai mult de 24 de ore pentru a finaliza sarcina.

Unul dintre primele lucruri pe care le putem face este să observăm că putem plasa doar o regină pe fiecare rând - imediat ce plasăm o regină pe un rând, fiecare alt pătrat în acel rând este sub atac. Deci, acum avem doar 8 * 8 * 8 * 8 * 8 * 8 * 8 * 8 combinații sau 16,777,216.

## Regulile Jocului

- **Plasarea Reginelor:**
  - Fiecare regină poate ocupa oricare dintre cele opt coloane ale tablei.
  - Nu pot exista două regine pe aceeași linie sau coloană.
  - O regină amenință orice pătrat de pe aceeași linie, coloană sau diagonală.


## Detalii de Implementare

Programul utilizează o soluție eficientă bazată pe backtracking și recursivitate pentru a explora toate configurațiile posibile și a găsi soluții valide. Algoritmul progresează prin plasarea reginelor pe tablă, verificând continuu dacă configurația curentă respectă regulile jocului.

Inițial, începem prin a așeza o regină în primul rând și continuăm prin plasarea reginei în rândurile ulterioare. În timpul acestei procesări, identificăm și eliminăm imediat combinațiile invalide odată ce găsim o configurație nereușită în primele rânduri.

De exemplu, dacă încercăm să plasăm o regină în colțul din dreapta sus, urmată de una direct sub ea, această configurație nu este validă. Prin urmare, toate combinațiile posibile care implica regine în aceste două poziții pot fi excluse din procesul de explorare. Apoi, revenim și plasăm a doua regină în al doilea pătrat. Dacă și această încercare nu reușește, continuăm cu a doua regină în al treilea pătrat, și așa mai departe. Acest proces se repetă până când găsim o soluție sau până când am explorat toate variantele posibile.

## Utilizare

1. Utilizatorul este solicitat să introducă numărul dorit de regine (între 4 și 10).
2. Programul generează și afișează soluțiile găsite.
3. Utilizatorul decide dacă dorește să salveze soluțiile într-un fișier text, având posibilitatea de a specifica un nume pentru fișier.

Pentru a utiliza acest program, asigurați-vă că aveți instalat modulul `colorama`. Puteți instala acest modul folosind comanda:
```bash
pip install colorama
```