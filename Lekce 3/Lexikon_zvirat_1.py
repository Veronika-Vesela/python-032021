import pandas
import requests

# r = requests.get("https://raw.githubusercontent.com/lutydlitatova/czechitas-datasets/main/datasets/lexikon-zvirat.csv")
# open("lexikon-zvirat.csv", "wb").write(r.content)

zvirata=pandas.read_csv("lexikon-zvirat.csv", sep=";")

# Poslední sloupec a poslední řádek obsahují nulové hodnoty. Zbav se tohoto sloupce a řádku.
zvirata=zvirata.dropna(how="all", axis="columns")
zvirata=zvirata.dropna(how="all", axis="rows")

# Nastav sloupec id jako index pomocí metody set_index.
zvirata=zvirata.set_index("id")

def check_url (radek):
    if isinstance(radek.image_src, str):
        if radek.image_src.startswith("https://zoopraha.cz/images/"):
            if (radek.image_src.endswith("jpg")):
                return "OK"
            else:
                return "chyba"
        else:
            return "chyba"
    else:
        return "chyba"



seznam_chybna_zvirata=[]
for radek in zvirata.itertuples():
    if check_url(radek) == "chyba":
        seznam_chybna_zvirata.append(radek.title)

print(seznam_chybna_zvirata)


# #vypsání pomocí pomocného sloupečku - není ideální
# zvirata["kontrola_obrazek"]="zatím nezkontrolováno"
# seznam_kontrol_obrazek=[]
# for radek in zvirata.itertuples():
#     seznam_kontrol_obrazek.append(check_url(radek))
# zvirata["kontrola_obrazek"]=seznam_kontrol_obrazek
#
# zvirata_chybna=zvirata[zvirata["kontrola_obrazek"]=="chyba"]
# print(zvirata_chybna["title"])



