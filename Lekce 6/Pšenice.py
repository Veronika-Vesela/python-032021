import pandas
import requests
from scipy.stats import mannwhitneyu

# with requests.get("https://raw.githubusercontent.com/pesikj/progr2-python/master/data/psenice.csv") as r:
#   open("psenice.csv", 'w', encoding="utf-8").write(r.text)
#

# V souboru jsou data o délce zrn pšenice v milimetrech pro dvě odrůdy - Rosa a Canadian.
# Proveď statistický test hypotézy o tom, zda se délka těchto dvou zrn liší.
# K testu použij Mann–Whitney U test, který jsme používali na lekci.
data=pandas.read_csv("psenice.csv")
x = data["Rosa"]
y = data["Canadian"]
print(mannwhitneyu(x,y,alternative="two-sided")

# H0 = Délka zrn je stejná
# H1 = Délka zrn se liší

# P hodnota je nižší než hladina významnosti, proto zamítáme nulovou hypotézu. Délka zrn se tedy liší.

