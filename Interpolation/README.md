# Interpolation Numérique

Application web interactive pour visualiser les méthodes d'interpolation numérique.

## Méthodes implémentées

- **Interpolation Linéaire** : relie les points par des droites
- **Interpolation de Lagrange** : polynôme unique passant par tous les points
- **Splines Quadratiques** : polynômes de degré 2 par morceaux

## Structure du projet
Interpolation/
│
├── lineaire.py     → Interpolation linéaire
├── lagrange.py     → Interpolation de Lagrange
├── splines.py      → Splines quadratiques
├── app.py          → Interface web Streamlit
└── README.md       → Documentation
## Installation

```bash
pip install numpy sympy scipy matplotlib streamlit
```

## Lancer l'application

```bash
streamlit run app.py
```

## Technologies utilisées

- **Python** : langage de programmation
- **NumPy** : calculs numériques
- **SymPy** : calculs symboliques et Lambdify
- **Matplotlib** : graphiques
- **Streamlit** : interface web
## Bilan final
Interpolation/
│
├── lineaire.py     ✅ code + docstring
├── lagrange.py     ✅ code + docstring
├── splines.py      ✅ code + docstring
├── app.py          ✅ interface Streamlit
└── README.md       ✅ documentation