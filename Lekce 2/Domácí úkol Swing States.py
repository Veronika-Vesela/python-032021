import pandas
import requests
import numpy

# with requests.get("https://raw.githubusercontent.com/pesikj/progr2-python/master/data/1976-2020-president.csv") as r:
#   open("1976-2020-president.csv", 'w', encoding="utf-8").write(r.text)

presidenti=pandas.read_csv("1976-2020-president.csv")


# Urči pořadí jednotlivých kandidátů v jednotlivých státech a v jednotlivých letech (pomocí metody rank()).
# Nezapomeň, že data je před použitím metody nutné seřadit a spolu s metodou rank() je nutné použít metodu groupby().
presidenti_sorted=presidenti.sort_values(by=["year","state","candidatevotes"])
presidenti_sorted["rank"]=presidenti_sorted.groupby(["year", "state"])["candidatevotes"].rank(ascending=False)

# Pro další analýzu jsou důležití pouze vítězové. Ponech si v tabulce pouze řádky, které obsahují vítěze voleb v jednotlivých letech v jednotlivých státech.
presidenti_vitezove=presidenti_sorted[presidenti_sorted["rank"]==1]


# Pomocí metody shift() přidej nový sloupec, abys v jednotlivých řádcích měl(a) po sobě vítězné strany ve dvou po sobě jdoucích letech.
presidenti_vitezove=presidenti_vitezove.sort_values(by=["state", "year"])
presidenti_vitezove["party_last_year"]=presidenti_vitezove.groupby(["state"])["party_simplified"].shift(-1)
presidenti_vitezove.to_csv("presidenti_vitezove.csv")


# Porovnej, jestli se ve dvou po sobě jdoucích letech změnila vítězná strana.
# Můžeš k tomu použít např. funkce numpy.where a vložit hodnotu 0 nebo 1 podle toho, jestli došlo ke změně vítězné strany.

presidenti_vitezove=presidenti_vitezove.dropna(subset=["party_last_year"])
presidenti_vitezove["zmena_proti_lonsku"]=numpy.where(presidenti_vitezove["party_simplified"]==presidenti_vitezove["party_last_year"],0,1)



# Proveď agregaci podle názvu státu a seřaď státy podle počtu změn vítězných stran.
staty_pocet_zmen=pandas.DataFrame(presidenti_vitezove.groupby(["state"])["zmena_proti_lonsku"].sum())
staty_pocet_zmen=staty_pocet_zmen.sort_values(by=["zmena_proti_lonsku"])
print(staty_pocet_zmen)