# Interpolation Numérique

Projet réalisé dans le cadre du cours d'Analyse Numérique (Séance 03/03/26).

## Description
Ce projet implémente deux méthodes d'interpolation numérique en Python :
- **Interpolation de Lagrange**
- **Spline Quadratique**

## Structure du projet
interpolation/
├── lagrange.py    # Interpolation de Lagrange
├── splines.py     # Spline Quadratique
├── main.py        # Tests et graphiques locaux
├── app.py         # Application web Streamlit
└── README.md      # Documentation

## Prérequis
- Python 3.x
- NumPy
- Matplotlib
- Streamlit

## Installation
pip install numpy matplotlib streamlit

## Utilisation

### Lancer l'application web
streamlit run app.py

### Lancer les tests locaux
python main.py

## Méthodes implémentées

### 1. Interpolation de Lagrange
Le polynôme de base :
Li(x) = ∏ (x - xj) / (xi - xj)   j≠i

Le polynôme interpolateur :
P(x) = Σ yj * Lj(x)

### 2. Spline Quadratique
Formule du morceau i :
Si(x) = (1/2) * (zi+1 - zi)/(xi+1 - xi) * (x - xi)² + zi*(x - xi) + yi

Récurrence :
zi+1 = 2 * (yi+1 - yi)/(xi+1 - xi) - zi

## Auteur
- Nom : Zah Bi Zah Wilfried Vianney
- Cours : Analyse Numérique
- Date : 03/03/2026