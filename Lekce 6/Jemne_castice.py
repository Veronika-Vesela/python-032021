import requests
import pandas
from scipy.stats import mannwhitneyu

with requests.get("https://raw.githubusercontent.com/pesikj/progr2-python/master/data/air_polution_ukol.csv") as r:
  open("air_polution_ukol.csv", 'w', encoding="utf-8").write(r.text)

znecisteni=pandas.read_csv("air_polution_ukol.csv")
znecisteni["date"]=pandas.to_datetime(znecisteni["date"])
znecisteni=znecisteni.sort_values(by="date", ascending=False)
# print(znecisteni)

# Z dat vyber data za leden roku 2019 a 2020.

znecisteni["month"]=znecisteni["date"].dt.month
znecisteni["year"]=znecisteni["date"].dt.year
leden=znecisteni[znecisteni["month"]==1]
leden_2019=leden[leden["year"]==2019]
leden_2020=leden[leden["year"]==2020]
print(leden_2019)
print(leden_2020)



# Porovnej průměrné množství jemných částic ve vzduchu v těchto dvou měsících pomocí Mann–Whitney U testu.
# Formuluj hypotézy pro oboustranný test (nulovou i alternativní) a napiš je do komentářů v programu.

x=leden_2019["pm25"]
y=leden_2020["pm25"]
print(mannwhitneyu(x,y,alternative="two-sided"))

# H0 = množství jemnách částic je v obou měsících stejné.
# H1 = množství částic se v jednotlivých měsících liší.

# Jelikož je p-hodnota nižšní než hladina významnosti, zamítáme nulovou hypotézu.
