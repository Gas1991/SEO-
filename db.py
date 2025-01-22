import streamlit as st
import pandas as pd
import pymongo

# Connexion à MongoDB
client = pymongo.MongoClient("mongodb+srv://gas1991:gqsYfsbyCHfv2WjX@cluster0.9y1kj.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
db = client["Janvier"]
collection = db["Tendances"]

# Chargement des données depuis MongoDB
df = pd.DataFrame(list(collection.find()))
df = df.drop(columns=["_id"], errors="ignore")  # Supprime la colonne `_id`

# Trier les données et sélectionner les top résultats
top_df = df.sort_values(by="Mots clŽs sur Google", ascending=False).head(100)  # Top 10 résultats

st.title("SEO PERFORMANCE")
st.sidbar()

# Afficher le graphique
col_1,col_2 = st.columns(2)
with col_1:
    st.subheader("Tendance janvier 2024")
    st.dataframe(df)
    st.divider()
with col_2:
    st.subheader("Top 100")
    st.divider()
    st.bar_chart(top_df.set_index("Mots clŽs sur Google")["Visites"])
