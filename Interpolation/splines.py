"""
Module d'interpolation par splines quadratiques.
Utilise SymPy pour les expressions symboliques
et Lambdify pour l'évaluation numérique.
"""

import numpy as np
import sympy as sp
from sympy import lambdify

x = sp.symbols('x')

def spline_quadratique(points_x, points_y, x_eval, z0=0):
    """
    Calcule l'interpolation par splines quadratiques en un point x_eval.
    
    Paramètres :
    ------------
    points_x : list
        Liste des valeurs x des points de données.
        Exemple : [1, 2, 3, 4]
    points_y : list
        Liste des valeurs y des points de données.
        Exemple : [1, 4, 9, 16]
    x_eval : float
        Valeur de x où on veut évaluer l'interpolation.
        Exemple : 2.5
    z0 : float, optionnel
        Valeur initiale de la dérivée (par défaut 0).
    
    Retourne :
    ----------
    resultat : float
        Valeur numérique de l'interpolation en x_eval.
    Si : sympy expression
        Expression symbolique du morceau interpolateur.
    
    Exemple :
    ---------
    >>> points_x = [1, 2, 3, 4]
    >>> points_y = [1, 4, 9, 16]
    >>> resultat, Si = spline_quadratique(points_x, points_y, 2.5)
    >>> print(resultat)  # 6.75
    """
    
    n = len(points_x)
    
    # Étape 1 : Calculer les zi par récurrence
    z = [z0]
    i = 0
    while i < n - 1:
        zi1 = 2 * (points_y[i+1] - points_y[i]) / (points_x[i+1] - points_x[i]) - z[i]
        z.append(zi1)
        i = i + 1
    
    # Étape 2 : Trouver l'intervalle où se trouve x_eval
    i = 0
    while i < n - 2 and points_x[i+1] < x_eval:
        i = i + 1
    
    # Étape 3 : Construire Si(x) symboliquement
    xi  = points_x[i]
    xi1 = points_x[i+1]
    yi  = points_y[i]
    zi  = z[i]
    zi1 = z[i+1]
    
    Si = (zi1 - zi) / (2 * (xi1 - xi)) * (x - xi)**2 + zi * (x - xi) + yi
    
    # Étape 4 : Lambdifier et évaluer
    Si_func = lambdify(x, Si)
    resultat = Si_func(x_eval)
    
    return resultat, Si

# TEST
if __name__ == "__main__":
    points_x = [1, 2, 3, 4]
    points_y = [1, 4, 9, 16]
    x_eval = 2.5
    resultat, Si = spline_quadratique(points_x, points_y, x_eval)
    print("Formule symbolique :", sp.expand(Si))
    print("Résultat en x =", x_eval, ":", resultat)