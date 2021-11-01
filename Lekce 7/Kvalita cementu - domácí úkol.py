# V souboru Concrete_Data_Yeh.csv najdeš informace o kvalitě cementu.
import pandas
import matplotlib.pyplot as plt
import requests
import statsmodels.formula.api as smf
import seaborn
r = requests.get("https://raw.githubusercontent.com/pesikj/progr2-python/master/data/Concrete_Data_Yeh.csv")
with open("Concrete_Data_Yeh.csv", "wb") as f:
  f.write(r.content)

# Sloupce 1-7 udávají množství jednotlivých složek v kg, které byly přimíchány do krychlového metru betonu
# (např. cement, voda, kamenivo, písek atd.).
# Ve sloupci 8 je stáří betonu a ve sloupci 9 kompresní síla betonu v megapascalech.

beton=pandas.read_csv("Concrete_Data_Yeh.csv")

print(beton.isna().sum())
# je to OK, žádné nevyplněné hodnoty

mod=smf.ols(formula="csMPa ~ cement + slag + flyash + water + coarseaggregate + fineaggregate + age", data=beton)
res=mod.fit()
print(res.summary())


# Vytvoř regresní model, který bude predikovat kompresní sílu betonu na základě všech množství jednotlivých složek a jeho stáří.
# Zhodnoť kvalitu modelu.

# jelikož je hodnota R-squared: 0.612,


# Tipni si, která ze složek betonu ovlivňuje sílu betonu negativní (tj. má záporný regresní koeficient).
# Napiš, o kterou složku jde, do komentáře svého programu.

# jedná se o Vodu (s regresním koecifientem -0,2163.) - čím víc vody, tím menší zátěž beton vydrží