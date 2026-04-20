"""
Module d'interpolation de Lagrange.
Utilise SymPy pour les expressions symboliques
et Lambdify pour l'évaluation numérique.
"""

import numpy as np
import sympy as sp
from sympy import lambdify

x = sp.symbols('x')

def lagrange(points_x, points_y, x_eval):
    """
    Calcule l'interpolation de Lagrange en un point x_eval.
    
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
    P : sympy expression
        Expression symbolique du polynôme interpolateur.
    
    Exemple :
    ---------
    >>> points_x = [1, 2, 3, 4]
    >>> points_y = [1, 4, 9, 16]
    >>> resultat, P = lagrange(points_x, points_y, 2.5)
    >>> print(resultat)  # 6.25
    """
    
    n = len(points_x)
    P = 0
    
    # Double boucle while pour calculer le polynôme de Lagrange
    i = 0
    while i < n:
        Li = 1
        j = 0
        while j < n:
            if j != i:
                Li = Li * (x - points_x[j]) / (points_x[i] - points_x[j])
            j = j + 1
        P = P + points_y[i] * Li
        i = i + 1
    
    # Lambdifier et évaluer
    P_func = lambdify(x, P)
    resultat = P_func(x_eval)
    
    return resultat, P

# TEST
if __name__ == "__main__":
    points_x = [1, 2, 3, 4]
    points_y = [1, 4, 9, 16]
    x_eval = 2.5
    resultat, P = lagrange(points_x, points_y, x_eval)
    print("Formule symbolique :", sp.expand(P))
    print("Résultat en x =", x_eval, ":", resultat)