import streamlit as st

# Configuration de la page
st.set_page_config(page_title="CV | Malick Pape MBAYE", page_icon="💎", layout="centered")

# --- STYLE CSS PERSONNALISÉ (THÈME MINÉRAL & OR) ---
st.markdown("""
    <style>
    /* Fond dégradé effet pierre/minéral */
    .stApp {
        background: linear-gradient(135deg, #e0e0e0 0%, #bdc3c7 100%);
    }
    
    /* Cartes Glassmorphism avec bordure dorée */
    .main-card {
        background: rgba(255, 255, 255, 0.9);
        padding: 25px;
        border-radius: 15px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.1);
        border-left: 8px solid #D4AF37; /* Couleur Or */
        margin-bottom: 20px;
        color: #2c3e50;
    }

    /* Badges de compétences dorés */
    .skill-badge {
        display: inline-block;
        background: #D4AF37;
        color: #1a1a1a;
        padding: 6px 14px;
        border-radius: 5px;
        margin: 4px;
        font-size: 0.85em;
        font-weight: bold;
        text-transform: uppercase;
        border: 1px solid #b8860b;
    }

    /* Titres */
    h1, h2, h3 {
        color: #1a1a1a !important;
        font-family: 'Arial Black', sans-serif;
    }
    
    .contact-text {
        font-size: 1.1em;
        margin-bottom: 5px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- BARRE LATÉRALE ---
with st.sidebar:
    st.markdown("<h2 style='color: #D4AF37;'>📍 Contact</h2>", unsafe_allow_html=True)
    st.markdown(f"""
    <div class='contact-text'>👤 <b>Malick Pape MBAYE</b></div>
    <div class='contact-text'>📞 76 533 80 65</div>
    <div class='contact-text'>📧 <a href='mailto:malickpapembaye221@gmail.com'>Email</a></div>
    <div class='contact-text'>🏠 Dakar, Sénégal</div>
    """, unsafe_allow_html=True)
    
    st.divider()
    
    st.markdown("<h2 style='color: #D4AF37;'>🌍 Langues</h2>", unsafe_allow_html=True)
    st.write("**Français** : Maternel / Avancé")
    st.progress(95)
    st.write("**Anglais** : Niveau Intermédiaire")
    st.progress(60)

# --- EN-TÊTE ---
st.title("🌍 MALICK PAPE MBAYE")
st.subheader("Étudiant en Géomatique | Expert en Données Spatiales")

# --- PROFIL ---
st.markdown(f"""
<div class="main-card">
    <h3>🧠 Profil Professionnel</h3>
    <p>Passionné par l'exploitation des ressources minérales et la topographie de précision. 
    Mon objectif est d'allier mes compétences techniques en SIG et dessin de plan pour 
    optimiser les projets d'extraction et d'aménagement. <b>Sérieux, organisé et orienté résultats.</b></p>
</div>
""", unsafe_allow_html=True)

# --- COMPÉTENCES ---
st.markdown("### 🛠 Expertise Technique")
col1, col2 = st.columns(2)

with col1:
    st.markdown("**Analyse & SIG**")
    sig = ["QGIS", "ArcGIS", "Analyse spatiale", "Géoréférencement"]
    for s in sig:
        st.markdown(f'<span class="skill-badge">{s}</span>', unsafe_allow_html=True)

with col2:
    st.markdown("**Topographie & Dessin**")
    topo = ["Dessin de plan", "Topographie", "Raster & Vectoriel", "Gestion de BDD"]
    for t in topo:
        st.markdown(f'<span class="skill-badge">{t}</span>', unsafe_allow_html=True)

# --- PROJETS ACADÉMIQUES ---
st.markdown("### 📽️ Projets Réalisés")

tab1, tab2, tab3 = st.tabs(["💎 Exploitation Zircon", "🗺️ Occupation du sol", "📐 Numérisation"])

with tab1:
    st.write("**Objectif :** Étude de faisabilité spatiale pour l'extraction de zircon.")
    st.write("- Analyse des couches géologiques.")
    st.write("- Calcul de surfaces et volumes pour l'exploitation.")

with tab2:
    st.write("**Objectif :** Suivi environnemental et classification.")
    st.write("- Traitement d'images satellites pour identifier les changements du sol.")

with tab3:
    st.write("**Objectif :** Modernisation d'archives cartographiques.")
    st.write("- Géoréférencement de plans anciens et vectorisation sous QGIS.")

# --- FORMATION ---
st.markdown("### 🎓 Parcours Académique")
st.markdown("""
<div class="main-card">
    <b>BTS en Géomatique</b> • <i>En cours</i><br>
    <b>Baccalauréat Littéraire</b><br>
    <b>BEFEM</b>
</div>
""", unsafe_allow_html=True)

# --- LOISIRS ---
st.markdown("### 🎨 Loisirs & Intérêts")
c1, c2, c3 = st.columns(3)
with c1:
    st.info("⚡ **Nouvelles Tech**")
with c2:
    st.info("📖 **Lecture**")
with c3:
    st.info("⚽ **Sport**")

# --- BOUTON DE CONTACT ---
st.divider()
if st.button("🚀 DISCUTONS DE VOTRE PROJET"):
    st.balloons()
    st.success("Appelez-moi au 76 533 80 65 pour une collaboration immédiate !")