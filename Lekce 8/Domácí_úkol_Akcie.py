# Pomocí modulu yfinance, který jsme používali v 5. lekci, stáhni ceny akcií společnosti Cisco (používají "Ticker" CSCO)
# za posledních 5 let. Dále pracuj s cenami akcie v závěru obchodního dne, tj. použij sloupec "Close".

import yfinance as yf
import pandas
Cisco=yf.Ticker("CSCO")
Cisco_data=Cisco.history(period="5y")
Cisco_data.describe()
# Cisco_data=Cisco_data.set_index("Date")
Cisco_close=pandas.DataFrame(Cisco_data["Close"])
Cisco_close["Date"]=Cisco_close.index
print(Cisco_close["Date"])


#
# # Zobraz si graf autokorelace a podívej se, jak je hodnota ceny závislná na svých vlastních hodnotách v minulosti.
from statsmodels.graphics.tsaplots import plot_acf
import matplotlib.pyplot as plt
print(Cisco_close["Close"].autocorr(lag=1))
plot_acf(Cisco_close["Close"])
plt.show()

# # Zkus použít AR model k predikci cen akcie na příštích 5 dní.
from statsmodels.tsa.ar_model import AutoReg
Cisco_close=Cisco_close.set_index("Date")
model=AutoReg(Cisco_close["Close"], lags=30, seasonal=False)
model_fit=model.fit()
predictions=model_fit.predict(start=Cisco_close.shape[0], end=Cisco_close.shape[0]+5)
Cisco_predictions=pandas.DataFrame({"predictions": predictions})
Cisco_close_with_prediction=pandas.concat([Cisco_close,Cisco_predictions])
Cisco_close_with_prediction_tail=Cisco_close_with_prediction.tail(100)
print(Cisco_close_with_prediction)
Cisco_close_with_prediction_tail.plot()
plt.show()
#
# # Zobraz v grafu historické hodnoty (nikoli celou řadu, ale pro přehlednost např. hodnoty za posledních 50 dní) a tebou vypočítanou predikci.