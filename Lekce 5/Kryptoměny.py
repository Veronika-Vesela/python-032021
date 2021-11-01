import pandas
import requests
import pandas
import seaborn
import matplotlib.pyplot as plt
pandas.set_option("display.max_columns", None)


# r = requests.get("https://raw.githubusercontent.com/pesikj/progr2-python/master/data/crypto_prices.csv")
# open("crypto_prices.csv", "wb").write(r.content)

crypto=pandas.read_csv("crypto_prices.csv")
#
# Použij zavírací cenu kryptoměny (sloupec Close) a vypočti procentuální změnu jednotlivých kryptoměn.
# Pozor na to, ať se ti nepočítají ceny mezi jednotlivými měnami. Ošetřit to můžeš pomocí metody groupby(),
# jako jsme to dělali např. u metody shift().
crypto["Date"]=pandas.to_datetime(crypto["Date"])
crypto_pivot=pandas.pivot_table(crypto, values="Close", index="Date", columns="Name").sort_values(by="Date")
crypto_pivot_change = crypto_pivot.pct_change()
# print(crypto_pivot_change)

# # Vytvoř korelační matici změn cen jednotlivých kryptoměn a zobraz je jako tabulku.
crypto_corr=crypto_pivot_change.corr()
# print(crypto_corr)




# # V tabulce najdi nejvyšší hodnotu korelace a korelaci nejblíže 0.
print(crypto_corr.shape)
crypto_corr_abs= crypto_corr.abs()
# print(crypto_corr_abs)
crypto_pairs = crypto_corr_abs.unstack()
crypto_pairs_sorted = crypto_pairs.sort_values()
print(crypto_pairs_sorted)
print(crypto_pairs_sorted.head()) # Tether a Monero
print(crypto_pairs_sorted.iloc[-30:]) #Wrapped Bitcoin a Bitcoin


# Změny cen pro dvojice měn, které jsou nejvíce a nejméně korelované, si zobraz jako bodový graf.

seaborn.jointplot("Tether", "Monero", crypto_pivot_change, kind="scatter")
plt.show()
seaborn.jointplot("Wrapped Bitcoin", "Bitcoin", crypto_pivot_change, kind="scatter")
plt.show()
#


