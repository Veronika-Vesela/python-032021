from sklearn.datasets import load_digits
from sklearn.preprocessing import StandardScaler
from sklearn.manifold import TSNE
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
import matplotlib.pyplot as plt

digits = load_digits()
X = digits.data

# Data normalizuj

scaler=StandardScaler()
X=scaler.fit_transform(X)

# Redukuj počet vstupních proměnných na dvě pomocí TSNE. Můžeš vyzkoušet různé parametry.

tsne=TSNE(
    init = "pca",
    n_components=3,
    perplexity=20,
    learning_rate="auto",
    random_state=42
)
X=tsne.fit_transform(X)

# Vykresli data do bodového grafu. Kolik odhaduješ shluků (clusterů)?

plt.scatter(X[:,0],X[:,1], s=25)
plt.show()
print("Odhaduji 6 clusterů")


# Aplikuj algoritmus KMeans s počtem shluků, který jsi odhadl/a v předchozím kroku
model = KMeans(n_clusters=6, random_state = 42)
labels = model.fit_predict(X)
plt.scatter(X[:, 0], X[:, 1], c=labels, s=50, cmap="Set1")
centers = model.cluster_centers_
plt.scatter(centers[:, 0], centers[:, 1], c="black", s=200, alpha=0.5)
plt.show()


# Vyhodnoť výsledek pomocí silhouette_score, který by měl být alespoň 0.5

print(f"pri rozdělení na 6 clusterů nám silhouette score vyjde {silhouette_score(X,labels)}")
print("Můj odhad úplně nevyšel, pokud jsem v dokumentaci dohledala správně, mělo být clusterů 10")

model = KMeans(n_clusters=10, random_state = 42)
labels = model.fit_predict(X)
plt.scatter(X[:, 0], X[:, 1], c=labels, s=50, cmap="Set1")
centers = model.cluster_centers_
plt.scatter(centers[:, 0], centers[:, 1], c="black", s=200, alpha=0.5)
plt.show()
print(f"pri rozdělení na 10 clusterů nám silhouette score vyjde {silhouette_score(X,labels)}")