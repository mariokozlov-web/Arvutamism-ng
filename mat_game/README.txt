----------------
# PROJEKTI TEEMA
----------------
Arvutamismäng, mis on inspireeritud Miksikese pranglimise mängust. Tegemist on ajapõhise matemaatikamänguga, kus mängija peab lahendama arvutustehted enne, kui aeg otsa saab.

------------------
# PROJEKTI EESMÄRK
------------------
Projekti eesmärk on luua lihtne ja interaktiivne matemaatikamäng, mis aitab kasutajal harjutada peastarvutamist. Mäng genereerib juhuslikke arvutustehted (liitmine, lahutamine ja korrutamine, jagamine), mille raskusaste suureneb iga tasemega.

Mäng algab väiksemate arvudega, kuid iga uue tasemega muutuvad arvud suuremaks ja tehete lahendamine keerulisemaks. Samal ajal jookseb taimer, mis loendab aega nulli poole. Kui mängija vastab õigesti, saab ta aega juurde. Kui vastus on vale, võetakse aega vähemaks.

Programm kasutab tkinter graafilist kasutajaliidest (GUI). Kasutaja saab vastuse sisestada hiirega vajutatavate numbrinuppude abil, mis on kujundatud sarnaselt kalkulaatori klaviatuurile.

--------------------------
# See programm on kasulik:
--------------------------
* õpilastele, kes soovivad harjutada peastarvutamist
* kasutajatele, kes tahavad mängulisel viisil matemaatikat treenida
* programmeerimise õppimiseks
---------------------------

-------------------------------------
# Projektis plaanitud edasiarendused:
-------------------------------------
* scoreboard ehk tulemuste tabel, kus näeb varasemaid skoore
* naljakad GIF-id õige ja vale vastuse korral
* level süsteemi loogika parandamine, hetkel on tehete raskustase kaootiline


-------------------------
# PROJEKTI KASUTUSJUHISED
-------------------------
1. Programmi käivitamine

* Veendu, et arvutis on paigaldatud Python 3.
* Ava terminal või käsurida.
* Liigu kausta, kus asub fail.
* Käivita programm käsuga:

python "Calc Game 2.py"

2. Mängu eesmärk

* Lahenda ekraanile ilmuv matemaatika tehe enne, kui aeg otsa saab.

3. Kuidas mängida

* Ekraanile ilmub matemaatika tehe (näiteks: 7 + 3 = ?).
* Sisesta vastus vajutades hiirega numbrinuppe.
* Vajuta nuppu "VASTA", et kontrollida oma vastust.

4. Punktid ja aeg

* Õige vastus annab +5 sekundit aega.
* Vale vastus võtab −2 sekundit aega.
* Iga 5 õige vastuse järel tõuseb tase.

5. Tasemed

* Iga uue tasemega muutuvad arvud suuremaks.
* Seetõttu muutuvad tehted raskemaks.

6. Mängu lõpp

* Kui taimer jõuab nulli, saab mäng läbi.
* Ekraanile kuvatakse, mitu tehet õigesti vastasid


-------------------------
Kasutatud kursuse teemad:
-------------------------
Funktsioonid
Tingimuslaused (if / elif / else)
Tsüklid (while)
Sisseehitatud funktsioonid (nt int(), str())
GUI programmeerimine (tkinter)
Asünkroonsus / lõimed (threading)
Moodulite kasutamine (import)
Juhuslikkuse kasutamine (random)
Muutujad ja programmiloogika
