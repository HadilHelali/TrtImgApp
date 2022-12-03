import streamlit as st
from commun import *

# CSS to inject contained in a string
hide_table_row_index = """
            <style>
            thead tr:first-child {display:none}
            tbody th {display:none}
            </style>
            """

# Inject CSS with Markdown
st.markdown(hide_table_row_index, unsafe_allow_html=True)

st.title('Lecture et écriture')
lec, ecr = st.tabs(["Lecture", "Ecriture"])
# -------------- LECTURE ----------------
with lec:
    f = st.file_uploader("Importer une image :",type=(["pgm"]))
    if f is not None:
        path_in = f.name
        print(path_in)
        st.pyplot(showImage('images/'+path_in))
        # TODO : lecture de l'image
        with st.expander("Plus d'informations sur l'image"):
            st.table(
                [["taille",""],
                ["nombre de lignes",""],
                ["nombre de colonnes",""]],

            )
    else:
        path_in = None

# -------------- ECRITURE ----------------
with ecr:
    st.write("écriture")
    # TODO : écriture de l'image