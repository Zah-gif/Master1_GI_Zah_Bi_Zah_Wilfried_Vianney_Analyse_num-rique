import numpy as np
import matplotlib.pyplot as plt

# Fonction qui calcule Li(x)
def lagrange_basis(x, i, xpoints):
    Li = 1.0
    j = 0
    while j < len(xpoints):
        if j != i:
            Li *= (x - xpoints[j]) / (xpoints[i] - xpoints[j])
        j += 1
    return Li

# Fonction qui calcule P(x)
def lagrange_interpolation(x, xpoints, ypoints):
    Px = 0.0
    i = 0
    while i < len(xpoints):
        Px += ypoints[i] * lagrange_basis(x, i, xpoints)
        i += 1
    return Px