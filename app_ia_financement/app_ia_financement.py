import streamlit as st
import pathlib
from streamlit_extras.stylable_container import stylable_container

# Font definition and global config is in the config.toml file

# --- CSS styling ---

def load_css(file_path):
    with open(file_path) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
# Load custom CSS
css_path = pathlib.Path("styles.css")
load_css(css_path)

# --- Sidebar ---
st.sidebar.title("Mon Compte")
st.sidebar.image("img/logo_D4G_no_text.png", width=120)
st.sidebar.markdown("---")


# buttons sidebar
menu = ["📝 Nouveau formulaire", "📚 Bibliothèque", "ⓘ Guide d'utilisation"]
menu_keys = ["formulaire", "biblio", "guide"]
for item, key in zip(menu, menu_keys):
    st.sidebar.button(item, key=key)    


# --- Main header ---
st.title("DossierIA+")
st.header("Facilitez vos réponses aux demandes de subventions")
st.write("""DossierIA+ pré-remplit automatiquement vos formulaires à partir de vos documents sources. **En quelques clics, votre dossier est prêt !**  
         Vous gardez le contrôle pour les ajuster facilement, tout en gagnant un temps précieux. Conçue par et pour les associations, cette solution vous aide à maximiser l’impact de vos actions en vous permettant de vous concentrer sur l’essentiel.""")
st.divider() 

# --- Project uploading documents ---
st.header("Etape 1 - Chargez vos documents")
st.subheader("Votre projet")

# Drag and drop multiple files
uploaded_project_files = st.file_uploader("**Chargez les documents présentant votre projet** (note de cadrage, dossier de présentation, budget, annexes, etc.) ", 
    accept_multiple_files=True, type=['pdf', 'docx', 'csv'], key='proj')
if uploaded_project_files is not None:
    for uploaded_file in uploaded_project_files:
        st.write(f"Fichier {uploaded_file.name} importé avec succès.")
                
# Renaming and upload 1 file
col1, col2 = st.columns([4, 1], vertical_alignment="center")
with col1:
    proj_name = st.text_input("**Titre de votre projet**", placeholder="Ex. : Prévention des zoonoses au Cambodge", key='proj_name')

# Customizing the button by creating a container and using streamlit_extras.
with col2:
    with stylable_container(
        key="btn_proj",
        css_styles="""
            button { 
                background-color: #FFD1D2;border-color:black} """,):
            upload_button = st.button("Importer", key='btn_proj')

    if upload_button:
        if proj_name:
            st.success(f"Projet '{proj_name}' importé avec succès.")
        else:
            st.warning("Veuillez saisir un titre de projet avant d'importer.")

# Uploading documents from the library 
col1, col2 = st.columns([4, 1], vertical_alignment="center")
with col1:
    proj_lib = st.selectbox("Ou utilisez des documents de la bibliothèque", ["Présentation Projet Mahakam"], key='proj_lib')
with col2:
    with stylable_container(
        key="btn_proj_lib",
        css_styles="""
            button { 
                background-color: #A2A2A2; color:white} """,):
            upload_lib_button = st.button("Charger", key='btn_proj_lib')
    if upload_lib_button:
        st.success("Projet de la bibliothèque importé avec succès.")

   
        
# --- Association uploading documents ---
st.subheader("Votre association")

# Drag and drop multiple files
uploaded_asso_files = st.file_uploader("**Chargez les documents présentant votre association** (présentation institutionnelle, statuts, rapports d’activité, etc.)) ", 
    accept_multiple_files=True, type=['pdf', 'docx', 'csv'], key='assoc')
if uploaded_asso_files is not None:
    for uploaded_file in uploaded_asso_files:
        st.write(f"Fichier {uploaded_file.name} importé avec succès.")
                
# Renaming and upload 1 file
col1, col2 = st.columns([4, 1], vertical_alignment="center")
with col1:
    assoc_name = st.text_input("**Nom associé aux fichiers**", placeholder="Ex : Présentation Forêts en Danger", key='assoc_name')

# Customizing the button by creating a container and using streamlit_extras.
with col2:
    with stylable_container(
        key="btn_asso",
        css_styles="""
            button { 
                background-color: #FFD1D2;border-color:black} """,):
            upload_button = st.button("Importer", key='btn_asso')

    if upload_button:
        if assoc_name:
            st.success(f"Projet '{assoc_name}' importé avec succès.")
        else:
            st.warning("Veuillez saisir un titre de projet avant d'importer.")

# Uploading documents from the library 
col1, col2 = st.columns([4, 1], vertical_alignment="center")
with col1:
    assoc_lib = st.selectbox("Ou utilisez des documents de la bibliothèque", ["Présentation Projet Mahakam"], key='assoc_lib')
with col2:
    with stylable_container(
        key="btn_assoc_lib",
        css_styles="""
            button { 
                background-color: #A2A2A2; color:white} """,):
            upload_lib_button = st.button("Charger", key='btn_assoc_lib')
    if upload_lib_button:
        st.success("Projet de la bibliothèque importé avec succès.")



# --- Donate link button ---
st.link_button("Faire un don", "https://www.groupe-sos.org/faire-un-don/")