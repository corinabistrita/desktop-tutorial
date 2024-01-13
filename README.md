# Documentație - Problema Celor Opt Regine pe Tabla de Șah

## Găsirea Soluțiilor pentru Problema Reginelor

Acest program Python rezolvă problema plasării a unui număr specific de regine (de la 4 la 10 regine) pe o tablă de șah de dimensiune dată, astfel încât să nu existe conflicte între ele. Acesta oferă, de asemenea, opțiuni de afișare în consolă și salvare într-un fișier a soluțiilor găsite.

![Alt text](queen-solver-animation-6.gif)

## Regulile Jocului

- **Plasarea Reginelor:**
  - Fiecare regină poate ocupa oricare dintre cele opt coloane ale tablei.
  - Nu pot exista două regine pe aceeași linie sau coloană.
  - O regină amenință orice pătrat de pe aceeași linie, coloană sau diagonală.

- **Scopul Jocului:**
  - Plasarea tuturor celor opt regine pe tablă fără ca acestea să se amenințe reciproc.
  - Soluție pentru cele 8 Regine

Utilizarea forței brute și încercarea fiecărei combinații posibile de plasare a reginelor pe tablă duce la testarea a 4,426,165,368 de combinații. Dacă putem procesa 50,000 de combinații pe secundă, acest lucru ar dura mai mult de 24 de ore pentru a finaliza sarcina.

Unul dintre primele lucruri pe care le putem face este să observăm că putem plasa doar o regină pe fiecare rând - imediat ce plasăm o regină pe un rând, fiecare alt pătrat în acel rând este sub atac. Deci, acum avem doar 8 * 8 * 8 * 8 * 8 * 8 * 8 * 8 combinații sau 16,777,216.

Dacă algoritmul nostru funcționează prin plasarea unei regine în primul rând, apoi plasarea unei regine în al doilea rând, apoi în al treilea, putem elimina blocuri de combinații imediat ce găsim o combinație a primelor câteva rânduri care nu funcționează. De exemplu, plasarea unei regine în colțul din dreapta sus, urmată de una direct sub ea, nu funcționează. Prin urmare, toate combinațiile posibile care au regine în aceste două poziții pot fi ignorate. Apoi, revenim și plasăm a doua regină în al doilea pătrat. Din nou, această combinație nu funcționează, deci încercăm a doua regină în al treilea pătrat. De data aceasta regina este în siguranță, astfel că putem progresa la al treilea rând și să încercăm a treia regină în primul pătrat, etc. Această metodă de explorare a tuturor soluțiilor valide posibile prin parcurgerea soluției până când întâlniți o eroare și apoi să reveniți pentru a încerca o altă soluție alternativă se numește soluție de tip backtracking.

## Utilizare

1. Utilizatorul este solicitat să introducă numărul dorit de regine (între 4 și 10).
2. Programul generează și afișează soluțiile găsite.
3. Utilizatorul decide dacă dorește să salveze soluțiile într-un fișier text, având posibilitatea de a specifica un nume pentru fișier.

Pentru a utiliza acest program, asigurați-vă că aveți instalat modulul `colorama`. Puteți instala acest modul folosind comanda:
``` bash
pip install colorama
```