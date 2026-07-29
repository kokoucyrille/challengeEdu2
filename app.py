"""
app.py
======
Point d'entrée unique de l'application. Déclare explicitement les 5 pages du
tableau de bord via st.navigation (API moderne), ce qui remplace la découverte
automatique du dossier pages/ et évite l'entrée fantôme "app" qui apparaissait
en double avec "Accueil" dans le menu latéral natif.
"""
import streamlit as st

pages = [
    st.Page("pages/1_🏠_Accueil.py", title="Accueil", icon="🏠", default=True),
    st.Page("pages/2_📉_Marche_Emploi.py", title="Marché de l'emploi", icon="📉"),
    st.Page("pages/3_🏫_Formation_Professionnelle.py", title="Formation professionnelle", icon="🏫"),
    st.Page("pages/4_🧮_Analyses_Recommandations.py", title="Analyses & Recommandations", icon="🧮"),
    st.Page("pages/5_ℹ️_A_Propos.py", title="À propos", icon="ℹ️"),
]

st.navigation(pages).run()
