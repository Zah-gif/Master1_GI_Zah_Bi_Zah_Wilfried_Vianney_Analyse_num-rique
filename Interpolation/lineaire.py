"""
Module d'interpolation linéaire.
Utilise SymPy pour les expressions symboliques
et Lambdify pour l'évaluation numérique.
"""

import numpy as np
import sympy as sp
from sympy import lambdify

x = sp.symbols('x')

def interpolation_lineaire(points_x, points_y, x_eval):
    """
    Calcule l'interpolation linéaire en un point x_eval.
    
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
    
    Retourne :
    ----------
    resultat : float
        Valeur numérique de l'interpolation en x_eval.
    S : sympy expression
        Expression symbolique du polynôme interpolateur.
    
    Exemple :
    ---------
    >>> points_x = [1, 2, 3, 4]
    >>> points_y = [1, 4, 9, 16]
    >>> resultat, S = interpolation_lineaire(points_x, points_y, 2.5)
    >>> print(resultat)  # 6.5
    """
    
    # Trouver l'intervalle où se trouve x_eval
    i = 0
    while points_x[i+1] < x_eval:
        i = i + 1
    
    # Récupérer les bornes de l'intervalle
    xi  = points_x[i]
    xi1 = points_x[i+1]
    yi  = points_y[i]
    yi1 = points_y[i+1]
    
    # Construire le polynôme symbolique
    pente = (yi1 - yi) / (xi1 - xi)
    S = yi + pente * (x - xi)
    
    # Lambdifier et évaluer
    S_func = lambdify(x, S)
    resultat = S_func(x_eval)
    
    return resultat, S

# TEST
if __name__ == "__main__":
    points_x = [1, 2, 3, 4]
    points_y = [1, 4, 9, 16]
    x_eval = 2.5
    resultat, S = interpolation_lineaire(points_x, points_y, x_eval)
    print("Formule symbolique :", S)
    print("Résultat en x =", x_eval, ":", resultat)