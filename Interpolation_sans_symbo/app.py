import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from lagrange import lagrange_interpolation
from splines import spline_quadratique, calculer_z

st.title("Interpolation Numérique")
st.sidebar.header("Paramètres")

# Nombre de points
n = st.sidebar.slider("Nombre de points", min_value=2, max_value=10, value=4)

# Saisie des points
st.sidebar.subheader("Points de données")
xpoints = []
ypoints = []
i = 0
while i < n:
    col1, col2 = st.sidebar.columns(2)
    x_val = col1.number_input(f"x{i}", value=float(i))
    y_val = col2.number_input(f"y{i}", value=float(i))
    xpoints.append(x_val)
    ypoints.append(y_val)
    i += 1

xpoints = np.array(xpoints)
ypoints = np.array(ypoints)

# Condition initiale z0
st.sidebar.subheader("Condition initiale")
z0_option = st.sidebar.radio(
    "Choisir z0 :",
    ["Pente initiale", "z0 = 0", "Valeur personnalisée"]
)

if z0_option == "Pente initiale":
    z0 = (ypoints[1] - ypoints[0]) / (xpoints[1] - xpoints[0])
elif z0_option == "z0 = 0":
    z0 = 0.0
else:
    z0 = st.sidebar.number_input("Valeur de z0", value=0.0)

# Afficher les zi
st.subheader("Valeurs des zi (Spline)")
z = calculer_z(xpoints, ypoints, z0)
i = 0
while i < len(z):
    st.write(f"z{i} = {z[i]:.4f}")
    i += 1

# Méthodes à afficher
st.sidebar.subheader("Méthodes")
show_lagrange = st.sidebar.checkbox("Lagrange", value=True)
show_spline = st.sidebar.checkbox("Spline Quadratique", value=True)

# Points pour le tracé
x = np.linspace(min(xpoints), max(xpoints), 200)

# Graphique
fig, ax = plt.subplots(figsize=(10, 6))

if show_lagrange:
    y_lagrange = np.array([lagrange_interpolation(xi, xpoints, ypoints) for xi in x])
    ax.plot(x, y_lagrange, label="Lagrange", color="blue")

if show_spline:
    y_spline = np.array([spline_quadratique(xi, xpoints, ypoints, z0) for xi in x])
    ax.plot(x, y_spline, label="Spline Quadratique", color="green")

ax.scatter(xpoints, ypoints, color='red', zorder=5, label="Points donnés")
ax.legend()
ax.grid(True)
ax.set_title("Lagrange vs Spline Quadratique")
ax.set_xlabel("x")
ax.set_ylabel("y")

st.pyplot(fig)