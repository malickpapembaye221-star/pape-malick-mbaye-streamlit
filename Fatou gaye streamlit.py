import streamlit as st

# Configuration de la page
st.set_page_config(page_title="CV | Fatou Gaye", page_icon="📍", layout="wide")

# Style CSS personnalisé pour améliorer l'esthétique
st.markdown("""
    <style>
    .main {
        background-color: #f5f7f9;
    }
    .stHeader {
        background-color: #2e7d32;
        color: white;
        padding: 2rem;
        border-radius: 10px;
    }
    .skill-tag {
        display: inline-block;
        padding: 5px 12px;
        margin: 4px;
        background-color: #e8f5e9;
        border: 1px solid #2e7d32;
        border-radius: 15px;
        color: #2e7d32;
        font-weight: bold;
    }
    </style>
    """, unsafe_allow_html=True)

# --- BARRE LATÉRALE (SIDEBAR) ---
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/3135/3135715.png", width=150) # Remplace par ta photo
    st.title("Fatou Gaye")
    st.subheader("Étudiante en Géomatique")
    
    st.markdown("---")
    st.markdown("### 📞 Contact")
    st.write("📧 fatou2004.gaye@gmail.com")
    st.write("📱 +221 78 016 11 61")
    st.write("📍 Sénégal")
    
    st.markdown("---")
    st.markdown("### 🌍 Langues")
    st.write("**Français :** Avancé")
    st.write("**Anglais :** Intermédiaire")

# --- CORPS DU CV ---

# En-tête professionnel
st.markdown("""
    <div style="background-color:#1b5e20; padding:25px; border-radius:10px; text-align:center;">
        <h1 style="color:white; margin:0;">GÉOMATICIENNE</h1>
        <p style="color:#c8e6c9; font-size:1.2rem;">Analyse spatiale | Cartographie | SIG</p>
    </div>
    """, unsafe_allow_html=True)

st.write("\n")

# Profil
st.header("🧠 Profil Professionnel")
st.write("""
Passionnée par la géomatique et l'environnement, je me spécialise dans l'**Analyse des impacts de la coupe du bois** (cas particulier de la forêt de Missira à Tambacounda). 
Sérieuse, motivée et rigoureuse, je maîtrise les outils de collecte et de traitement de données spatiales pour répondre aux enjeux de l'aménagement du territoire.
""")

st.markdown("---")

# Compétences
st.header("💻 Compétences Techniques")
col1, col2 = st.columns(2)

with col1:
    st.subheader("SIG & Cartographie")
    skills_sig = ["QGIS", "ArcGIS", "Numérisation", "Géoréférencement", "Traitement Raster/Vectoriel"]
    for s in skills_sig:
        st.markdown(f'<span class="skill-tag">{s}</span>', unsafe_allow_html=True)

with col2:
    st.subheader("Données & Analyse")
    skills_data = ["Gestion de bases de données spatiales", "Analyse spatiale", "Occupation du sol", "Organisation"]
    for s in skills_data:
        st.markdown(f'<span class="skill-tag">{s}</span>', unsafe_allow_html=True)

st.write("\n")
st.markdown("---")

# Formation
st.header("🎓 Formation")
col_edu1, col_edu2 = st.columns([1, 4])
with col_edu1:
    st.write("**En cours**")
with col_edu2:
    st.write("**BTS en Géomatique**")
    
col_edu3, col_edu4 = st.columns([1, 4])
with col_edu3:
    st.write("**Diplôme**")
with col_edu4:
    st.write("**Baccalauréat Littéraire**")

st.markdown("---")

# Projets Académiques
st.header("🛠️ Projets Académiques")

with st.expander("📍 Numérisation et Géoréférencement"):
    st.write("Travaux de précision sur la mise en conformité de cartes anciennes et la création de couches vectorielles structurées.")

with st.expander("🏘️ Projet d'Aménagement du Territoire"):
    st.write("Analyse multidimensionnelle pour la planification urbaine et rurale.")

with st.expander("🌳 Cartographie de l'Occupation du Sol"):
    st.write("Étude de l'évolution des surfaces boisées et des zones agricoles via l'imagerie satellite.")

# Pied de page
st.markdown("---")
st.caption("CV Interactif généré avec Streamlit - 2024")