import pandas
import statistics

# Pokračuj v práci s daty o kryptoměnách.
# Z datového souboru si vyber jednu kryptoměnu a urči průměrné denní tempo růstu měny za sledované období. - Solana


crypto=pandas.read_csv("crypto_prices.csv")
crypto["Date"]=pandas.to_datetime(crypto["Date"])

# Vyber si sloupec se změnou ceny, kterou máš vypočítanou z předchozího cvičení (případně si jej dopočti)
crypto_pivot=pandas.pivot_table(crypto, values="Close", index="Date", columns="Name").sort_values(by="Date")
crypto_pivot_change = crypto_pivot.pct_change()
Solana=crypto_pivot_change[["Solana"]]
Solana=Solana.dropna()
# print(Solana)

# přičti k němu 1 (nemusíš dělit stem jako v lekci, hodnoty jsou jako desetinná čísla, nikoli jako procenta)
# a převeď jej na seznam pomocí metody .tolist().

Solana_growth_geom= []

for change in Solana["Solana"]:
    nove_pole= change + 1
    Solana_growth_geom.append(nove_pole)
print(Solana_growth_geom)

# Následně vypočti geometrický průměr z těchto hodnot.

print(statistics.geometric_mean(Solana_growth_geom)-1)
