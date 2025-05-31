import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# Daten für Histogramm erzeugen
data = np.random.normal(loc=0, scale=100, size=1000)  # Mittelwert=0, Std.Abw=1

# Histogramm erzeugen
bins = 20  # Anzahl der Bins
plt.hist(data, bins=bins, density=True, alpha=0.6, color="blue", edgecolor="black", label="Histogramm")

# Normalverteilung berechnen
x = np.linspace(min(data), max(data), 1000)
mu, sigma = np.mean(data), np.std(data)  # Mittelwert und Std.Abw aus Daten
y = norm.pdf(x, loc=mu, scale=sigma)

# Normalverteilung plotten
plt.plot(x, y, "r-", label=f"Normalverteilung\n$\mu={mu:.2f}$, $\sigma={sigma:.2f}$")

plt.title("Histogramm und Normalverteilung")
plt.xlabel("Werte")
plt.ylabel("Dichte")
plt.legend()
plt.show()
