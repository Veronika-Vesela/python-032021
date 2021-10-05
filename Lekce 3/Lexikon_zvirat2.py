# Chceme ke každému zvířeti vytvořit popisek na tabulku do zoo. Popisek bude využívat sloupců
#     - title (název zvířete),
#     - food (typ stravy),
#     - food_note (vysvětlující doplněk ke stravě) a
#     - description (jak zvíře poznáme).
# Napiš funkci popisek, která bude mít jeden parametr radek. Funkce spojí informace dohromady.
# Následně použijte metodu apply, abyste vytvořili nový sloupec s tímto popiskem.

import pandas
zvirata=pandas.read_csv("lexikon-zvirat.csv", sep=";")

def popisek (radek):
    title = str(radek.title)
    food = str(radek.food)
    food_note = str(radek.food_note)
    description = str(radek.description)
    popisek = title + " preferuje následující typ stravy:" + food + ". " + "Konkrétně ocení když mu do misky přistanou " + food_note + ". " + "\n" + "A jak toto zvíře vypadá? " + description
    return popisek

zvirata["Novy_popisek"]=zvirata.apply(popisek, axis = 1)
print(zvirata)


