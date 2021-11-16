import requests
import pandas
import matplotlib.pyplot as plt

# r = requests.get("https://raw.githubusercontent.com/pesikj/progr2-python/master/data/MLTollsStackOverflow.csv")
# with open("MLTollsStackOverflow.csv", "wb") as f:
#   f.write(r.content)


# Stáhni si soubor MLTollsStackOverflow.csv, který obsahuje počty položených otázek na jednotlivé programovací techniky a další technologie.
data=pandas.read_csv("MLTollsStackOverflow.csv")

# Vyber sloupec python.
data= data.set_index("month")
data_python=data[["python"]]
data_python.plot()
plt.show()

# Proveď dekompozici této časové řady pomocí multiplikativního modelu. Dekompozici zobraz jako graf.

from statsmodels.tsa.seasonal import seasonal_decompose
decompose=seasonal_decompose(data_python["python"], model="mul", period=12)
decompose.plot()
plt.show()

# Vytvoř predikci hodnot časové řady pomocí Holt-Wintersovy metody na 12 měsíců. Sezónnost nastav jako 12 a uvažuj multiplikativní model pro trend i sezónnost. Výsledek zobraz jako graf.
from statsmodels.tsa.holtwinters import ExponentialSmoothing
mod=ExponentialSmoothing(data_python["python"], seasonal_periods=12, trend="mul", seasonal="mul", initialization_method="estimated",)
res=mod.fit()
data_python_forecast=pandas.DataFrame(res.forecast(12), columns=["prediction"])
data_python_with_prediction=pandas.concat([data_python, data_python_forecast])
data_python_with_prediction[["python","prediction"]].plot()
plt.show()