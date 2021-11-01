import requests
import pandas
import statsmodels.formula.api as sfm
import matplotlib.pyplot as plt

r = requests.get("https://raw.githubusercontent.com/pesikj/progr2-python/master/data/Fish.csv")
with open("Fish.csv", "wb") as f:
  f.write(r.content)

# V souboru Fish.csv najdeš informace o rybách z rybího trhu:

# délku (vertikální - Length1, diagonální - Length2 a úhlopříčnou - Length3),
# výšku,
# šířku,
# živočišný druh ryby,
# hmnotnost ryby.

# Vytvoř regresní model, který bude predikovat hmnotnost ryby na základě její diagonální délky (sloupec Length2).
ryby=pandas.read_csv("Fish.csv")
model1=sfm.ols(formula="Weight ~ Length2", data=ryby)
res=model1.fit()
print(res.summary())
pred_ols=res.get_prediction()

plt.plot(ryby["Length2"], ryby["Weight"], "g.", )
plt.plot(ryby["Length2"], res.fittedvalues, "r")
plt.show()

# Zkus přidat do modelu výšku ryby (sloupec Height) a porovnej, jak se zvýšila kvalita modelu.
model2=sfm.ols(formula="Weight ~ Length2 + Height", data=ryby).fit()
print(model2.summary())
# R-squared se zvýšila z 0,844 na 0,875, model se tedy zpřesnil.

# Nakonec pomocí metody target encoding zapracuj do modelu živočišný druh ryb
ryby_prumer=ryby.groupby("Species")["Weight"].mean()
ryby["Species_weight_mean"]=ryby["Species"].map(ryby_prumer)

model3=sfm.ols(formula="Weight ~ Length2 + Height + Species_weight_mean", data=ryby).fit()
print(model3.summary())