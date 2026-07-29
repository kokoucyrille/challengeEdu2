"""
components/sidebar.py
======================
Rendu de la barre laterale : logo/titre du projet, rappel du contexte, puis
filtres globaux (delegues a components.filters). Les filtres ne sont affiches
que sur les pages qui en tirent une reelle valeur (show_filters=True) ; les
autres pages (Accueil, A propos, sections uniquement nationales) appellent
render_sidebar(show_filters=False) pour une interface plus sobre.
"""
import streamlit as st

from config import MINISTERE
from components.filters import render_page_filters, apply_filters
from utils.preprocessing import clean_etablissements


def render_sidebar(show_filters: bool = True, current: str = ""):
    """Affiche la sidebar complete et retourne (df_etab_filtre_ou_complet, filters_dict)."""
    with st.sidebar:
        st.markdown("**Adéquation Formation-Emploi**")
        st.caption(MINISTERE)
        st.caption("Data Challenge Éducation — Défi 2 — 2026")
        st.markdown("<hr>", unsafe_allow_html=True)

        df_etab = clean_etablissements()
        if show_filters:
            filters = render_page_filters(df_etab)
            df_filtered = apply_filters(df_etab, filters)
            st.caption(f"{len(df_filtered)} / {len(df_etab)} établissements pris en compte.")
        else:
            filters = {"regions": [], "annee_range": None}
            df_filtered = df_etab

    return df_filtered, filters
