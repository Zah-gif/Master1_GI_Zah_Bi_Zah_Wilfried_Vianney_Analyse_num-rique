from lagrange import lagrange_interpolation
from splines import spline_quadratique, calculer_z
import numpy as np
import matplotlib.pyplot as plt

# Points de données
xpoints = np.array([0.0, 1.0, 2.0, 3.0])
ypoints = np.array([1.0, 3.0, 2.0, 5.0])

# Condition initiale z0 = pente initiale
z0 = (ypoints[1] - ypoints[0]) / (xpoints[1] - xpoints[0])

# Afficher les zi
z = calculer_z(xpoints, ypoints, z0)
i = 0
while i < len(z):
    print(f"z{i} = {z[i]}")
    i += 1

# Points pour le tracé
x = np.linspace(0, 3, 100)
y_lagrange = np.array([lagrange_interpolation(xi, xpoints, ypoints) for xi in x])
y_spline = np.array([spline_quadratique(xi, xpoints, ypoints, z0) for xi in x])

# Graphique
plt.plot(x, y_lagrange, label="Lagrange", color="blue")
plt.plot(x, y_spline, label="Spline Quadratique", color="green")
plt.scatter(xpoints, ypoints, color='red', label="Points donnés")
plt.legend()
plt.grid(True)
plt.title("Lagrange vs Spline Quadratique")
plt.show()