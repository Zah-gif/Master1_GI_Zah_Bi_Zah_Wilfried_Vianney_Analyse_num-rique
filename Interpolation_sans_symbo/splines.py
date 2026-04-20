import numpy as np
import matplotlib.pyplot as plt

def calculer_z(xpoints, ypoints, z0=0):
    n = len(xpoints) - 1
    z = [0.0] * (n + 1)
    z[0] = z0
    i = 0
    while i < n:
        z[i+1] = 2 * (ypoints[i+1] - ypoints[i]) / (xpoints[i+1] - xpoints[i]) - z[i]
        i += 1
    return z

def trouver_intervalle(x, xpoints):
    i = 0
    while i < len(xpoints) - 1:
        if xpoints[i] <= x <= xpoints[i+1]:
            return i
        i += 1
    return len(xpoints) - 2

def spline_quadratique(x, xpoints, ypoints, z0=0):
    z = calculer_z(xpoints, ypoints, z0)
    i = trouver_intervalle(x, xpoints)
    hi = xpoints[i+1] - xpoints[i]
    Si = (1/2) * ((z[i+1] - z[i]) / hi) * (x - xpoints[i])**2 + z[i] * (x - xpoints[i]) + ypoints[i]
    return Si