import streamlit as st
import pymongo

client = pymongo.MongoClient("mongodb+srv://gas1991:gqsYfsbyCHfv2WjX@cluster0.9y1kj.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

headerSection = st.container()
mainSection = st.container()
LeftNav =st.sidebar
loginSection = st.container()
logOutSection= st.container()



def login():
    with headerSection:
        col_1,col_2=st.columns([2,1])
    
    with col_1:
        st.title("Page de connexion")
        
    with col_2:
        st.image("mytek.webp", width=200,)

    st.markdown("<h2 style='font-size: 25px; color: #333;'>Se connecter avec son compte</h2>", unsafe_allow_html=True)
    username = st.text_input("Identifiant")
    password = st.text_input("Mot de passe",type="password")
    if st.button("Se connecter"):
        if username == "admin" and password =="password":
            st.session_state.logged_in = True
            st.success("Login successful")
        else:
            st.error("invalid username or password")

def dashboard():
    with headerSection:
        st.title("Tendance Janvier 2025")        
    with LeftNav:
        st.text("hi")

    if st.button("sign out"):
        st.session_state.logged_in=False
        st.experimental_rerun()
if "logged_in" not in st.session_state:
    st.session_state.logged_in=False
if st.session_state.logged_in:
    dashboard()
else:
    login()
