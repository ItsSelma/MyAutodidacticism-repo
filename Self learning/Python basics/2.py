#baš kao u mnogim drugim programskim jezicima, python nudi i baratanje listama
#prije nego što ispišem kod, trebate razumjeti par stvari kako bi vam kod bio "čitljiv"
#[] označava praznu listu 
#append() dodaje elemente na kraj liste
#lista[]  pristupa elementu kojeg želimo, ovo je, na primjer, odlično za ispisivanje u printu ili korištenje sadržaja za računanje..

#eh, sada kada smo ovo sve prošli, možemo ispisati kod

mojaLista = []
mojaLista.append(1)
mojaLista.append(2)
mojaLista.append(3)
mojaLista.append(4)

print(mojaLista[0])
print(mojaLista[1])
print(mojaLista[2])
print(mojaLista[3])

#ovdje moramo paziti! ako pristupimo nekom elementu koji NE POSTOJI, dobit ćemo error

#print(mojaLista[10])

#superrr sada znamo raditi sa listama, hajdemo sada izvjezbati nešto što smo možda trebali i ranije.. a to su operatori :)
#baš kao u mnogim drugim programskim jezicima, možemo sabirati, oduzimati, dijeliti, množiti, modulirati(valjda se tako kaže)..

broj = 2 + 3 - 1 * 3 / 2
print(broj)

#modulo, najjednostavnije objašnjeno, za rezultat dobija "ono što ostane" od cjelobrojnog dijeljenja
# na primjer da cjelobrojno dijelimo 8/3, to bi bilo 6 sa "ostatkom" od 2, tako da je rezultat modul 2
#modulo pišemo sa %

modulo = 8%3
print(modulo)

#možemo i potencirati u pythonu, (3 na drugu, 3 na treću)...
#za potenciranje koristimo **

kub = 4 ** 3
print(kub)

#zanimljivo, operatori rade i sa stringovima

pozdraviMojuMnogobrojnuFamiliju = "ćaoo rode, " * 10
print(pozdraviMojuMnogobrojnuFamiliju)

#čak je moguće koristiti operatore i za liste
prvaLista = [1, 2, 3, 4, 5]
drugaLista = [6, 7, 8, 9, 10]
finalnaLista = prvaLista + drugaLista
print(finalnaLista)

veeelikaLista = prvaLista * 5
print(veeelikaLista)

#još jedna stvar zanimljiva u pythonu je formatiranje stringa
#koriste se simboli kao %s i %d

# %s je za umetanje stringa u tekst

ime = "Selma"

predstavljanje = "moje ime je %s" % ime

print (predstavljanje)

# %d se koristi za umetanje brojeva

godina = 22
predstavljanje2 = "moje ime je %s i imam %d godine" % (ime, godina)
print(predstavljanje2)


