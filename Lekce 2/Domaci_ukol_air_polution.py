import requests
import pandas
import numpy

with requests.get("https://raw.githubusercontent.com/pesikj/progr2-python/master/data/air_polution_ukol.csv") as r:
  open("air_polution_ukol.csv", 'w', encoding="utf-8").write(r.text)

znecisteni=pandas.read_csv("air_polution_ukol.csv")

# Načti dataset a převeď sloupec date (datum měření) na typ datetime.
znecisteni["date"]=pandas.to_datetime(znecisteni["date"])


# Přidej sloupce s rokem a číslem měsíce, které získáš z data měření.
znecisteni["year"]=znecisteni["date"].dt.year
znecisteni["month"]=znecisteni["date"].dt.month
znecisteni["period"]=znecisteni["date"].dt.year.astype(str)+"/"+znecisteni["date"].dt.month.astype(str)


# Vytvoř pivot tabulku s průměrným počtem množství jemných částic (sloupec pm25)
# v jednotlivých měsících a jednotlivých letech. Jako funkci pro agregaci můžeš použít numpy.mean.

pivot=pandas.pivot_table(znecisteni,values=["pm25"], index=["year"], columns=["month"], aggfunc=numpy.mean)
print(pivot)