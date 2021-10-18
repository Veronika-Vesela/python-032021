import requests
import pandas
import numpy
import seaborn
import matplotlib.pyplot as plt

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

# Podívej se do první lekce na část o teplotních mapách a zobrat výsledek analýzy jako teplotní mapu.
seaborn.heatmap(pivot, annot=True, fmt=".0f")
plt.show()

# Použij metodu dt.dayofweek a přidej si do sloupce den v týdnu. Číslování je od 0, tj. pondělí má číslo 0 a neděle 6.
znecisteni["day_of_week"]=znecisteni["date"].dt.dayofweek

# Porovnej, jestli se průměrné množství jemných částic liší ve všední dny a o víkendu.
# pivot_day_of_week=pandas.pivot_table(znecisteni, values=["pm25"], index=["day_of_week"], aggfunc=numpy.mean)
# print(pivot_day_of_week)

znecisteni_vsedni_dny=znecisteni[znecisteni["day_of_week"]<5]
znecisteni_vikend=znecisteni[znecisteni["day_of_week"]>4]
print("ZNEČISTĚNÍ V TÝDNU: ", znecisteni_vsedni_dny["pm25"].mean())
print("ZNEČISTĚNÍ O VÍKENDU: ", znecisteni_vikend["pm25"].mean())
