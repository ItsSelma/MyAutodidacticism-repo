#ovo je tradicionalni način kako započeti učenje bilo kojeg programskog ili skriptnog jezika
print ("Zdravo svijete!")

#vidimo da mi nismo morali da naglasimo int, double... to je zato što python automatski prepoznaje tip podatka
# kod if naredbe, nismo koristili () što ste se vjerovatno navikli ako koristite jezike kao c++ ili c#
#umjesto {} koristi se tipka "tab" koja se nalazi lijevo na tastaturi
# treba se navići koristiti ":" 

x=1
if x == 1:
    print("X je 1")

#eh, da nastavimo oko tipova podataka
#ovako bi definisali intider (brojevi kao 1, 2, 3.. ne 1.3352, 5.34)

#pored onog što sam spomenula oko prepoznavanja tipova podataka, u ovom dole kodu vidimo još jednu zanimljivu sitnicu koja mnogo znači :)
#u printu, ako želimo da ispišemo tekst, taj tekst stavljamo unutar "", a ako želimo da pozovemo varijablu, pišemo njen naziv bez ""

nekiint = 1
print(nekiint)

#okeeej, a kako onda da definišemo float (brojevi kao 1.3352, 5.34 )
#jednostavno! Naglasimo da će postojati broj nakon decimalnog zareza!

nekifloat = 1.0
print(nekifloat)

#postoji još jedan način, sa float()
nekifloat = float(2)
print(nekifloat)

#ako želimo string, koristimo "" ili '' i biti će automatski prepoznat string
nekistring = 'Hejjj '
print(nekistring)
nekistring = "Hejjjj ponovo"
print(nekistring)

#možda ste do sada primjetili da python "pregazi" predhodnu vrijednost varijable ako se ponovo nešto upiše u varijablu 

#Možemo reći da je "" prilagođen više ako pišemo na engleskom,šta ako trebamo napisati don't? radi ' ovdje moramo koristiti "" ("don't").

#možemo računati pomoću pythona!

jedan = 1
dva = 2
tri = jedan+dva
print(tri)

#nešto slično možemo uraditi i sa stringovima, ovo je odličan način da izbjegnemo ono "gaženje" predhodne vrijednosti

zdravo = "zdravo"
svijete = "svijete"

zdravoSvijete = zdravo+" "+svijete
print(zdravoSvijete)

#python dozvoljava i jednostavno "u nizu" dodavanje vrijednosti varijablama

a, b = 3, 4
print(a, b)

#moramo voditi računa na sljedeće, iako možemo od dva stringa napraviti veći string, od dva inta dobiti novi int, MIJEŠANJE različitih operatora nije omogućeno
one = 1
two = 2
zdravo = "zdravo"

#print(one + two + zdravo)

print ("Ćaooo :)")