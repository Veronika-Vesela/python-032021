import requests
import pandas

#r = requests.get("https://raw.githubusercontent.com/pesikj/python-032021/7cdd66d0313f60fe177fbdbd7f3b87b079cacd67/01_pandas/01/ukol/london_merged.csv?token=AVVCVO5LJYK5HYJQZKR5ASLBJGTJ4")
#open("london_merged.csv", 'wb').write(r.content)

# V souboru london_merged.csv najdeš informace o počtu vypůjčení jízdních kol v Londýně.
#
# Vytvoř sloupec, do kterého z časové značky (sloupec timestamp) ulož rok.
# Vytvoř kontingenční tabulku, která porovná kód počasí (sloupec weather_code se sloupcem udávající rok.
# Definice jednotlivých kódů jsou:
#
# 1 = Clear ; mostly clear but have some values with haze/fog/patches of fog/ fog in vicinity
# 2 = scattered clouds / few clouds
# 3 = Broken clouds
# 4 = Cloudy
# 7 = Rain/ light Rain shower/ Light rain
# 10 = rain with thunderstorm
# 26 = snowfall
# 94 = Freezing Fog

kola=pandas.read_csv("london_merged.csv")
kola["timestamp"]=pandas.to_datetime(kola["timestamp"])
kola["year"]=kola["timestamp"].dt.year

pivot=pandas.pivot_table(kola, index="weather_code", columns="year", aggfunc=len)
print(pivot)
