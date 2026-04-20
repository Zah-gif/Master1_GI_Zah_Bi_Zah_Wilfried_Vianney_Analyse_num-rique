import streamlit as st
import numpy as np
import sympy as sp
import matplotlib.pyplot as plt
from lineaire import interpolation_lineaire
from lagrange import lagrange
from splines import spline_quadratique

# Titre
st.title("Interpolation Numérique")
st.write("---")

# Sidebar
st.sidebar.title("Paramètres")
methode = st.sidebar.selectbox(
    "Choisir la méthode",
    ["Interpolation Linéaire", "Interpolation de Lagrange", "Splines Quadratiques"]
)

# Nombre de points
st.sidebar.write("---")
n_points = st.sidebar.number_input(
    "Nombre de points", 
    min_value=2, 
    max_value=10, 
    value=4
)

# Tableau de saisie
st.subheader("Entrer les points")
cols = st.columns(2)

points_x = []
points_y = []

i = 0
while i < n_points:
    with cols[0]:
        xi = st.number_input(f"x{i}", value=float(i+1), key=f"x{i}")
    with cols[1]:
        yi = st.number_input(f"y{i}", value=float((i+1)**2), key=f"y{i}")
    points_x.append(xi)
    points_y.append(yi)
    i = i + 1

# x à évaluer
st.write("---")
x_eval = st.number_input(
    "Valeur de x à évaluer", 
    value=2.5
)

# Bouton calculer
calculer = st.button("Calculer")

if calculer:
    if methode == "Interpolation Linéaire":
        resultat, formule = interpolation_lineaire(points_x, points_y, x_eval)
    elif methode == "Interpolation de Lagrange":
        resultat, formule = lagrange(points_x, points_y, x_eval)
    else:
        resultat, formule = spline_quadratique(points_x, points_y, x_eval)
    
    st.write("---")
    st.subheader("Résultats")
    
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Résultat", f"{resultat:.4f}")
    with col2:
        st.latex(sp.latex(formule))
# Graphique
    st.write("---")
    st.subheader("Graphique")
    
    # Créer les points pour la courbe
    x_courbe = np.linspace(min(points_x), max(points_x), 100)
    y_courbe = []
    
    i = 0
    while i < len(x_courbe):
        if methode == "Interpolation Linéaire":
            val, _ = interpolation_lineaire(points_x, points_y, x_courbe[i])
        elif methode == "Interpolation de Lagrange":
            val, _ = lagrange(points_x, points_y, x_courbe[i])
        else:
            val, _ = spline_quadratique(points_x, points_y, x_courbe[i])
        y_courbe.append(val)
        i = i + 1
    
    # Tracer le graphique
    fig, ax = plt.subplots()
    ax.plot(x_courbe, y_courbe, 'b-', label='Courbe interpolée')
    ax.scatter(points_x, points_y, color='green', zorder=5, label='Points donnés')
    ax.scatter(x_eval, resultat, color='red', zorder=5, s=100, label=f'x={x_eval} → y={resultat:.4f}')
    ax.legend()
    ax.grid(True)
    ax.set_title(methode)
    
    st.pyplot(fig)