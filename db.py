import streamlit as st
import pandas as pd
import pymongo

# Connexion à MongoDB
@st.cache_resource
def get_mongo_connection():
    client = pymongo.MongoClient("mongodb://gas1991:jYUxFL03Fzw2v1P7@localhost:27017/")
    return client

# Initialisation de la base de données et de la collection
client = get_mongo_connection()
db = client["Tendances"]
collection = db["Janvier"]

# Chargement des données depuis MongoDB
@st.cache_data(ttl=600)
def load_data():
    data = pd.DataFrame(list(collection.find()))
    data = data.drop(columns=["_id"], errors="ignore")  # Supprimer `_id` si elle existe
    return data

df = load_data()

# Trier les données et sélectionner les résultats principaux
top_df = df.sort_values(by="Event count", ascending=False).head(100)

# Affichage dans Streamlit
st.title("Analyse des tendances - Janvier 2024")

col_1, col_2 = st.columns(2)

with col_1:
    st.subheader("Toutes les données")
    st.dataframe(df)
    st.divider()

with col_2:
    st.subheader("Top 100 - Tendances")
    st.divider()
    st.bar_chart(top_df.set_index("Search term")["Event count"])
