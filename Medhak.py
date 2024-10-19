import streamlit as st


left, right = st.columns(2)
if left.button("Login with Existing Account", use_container_width=True):
  st.write("Login")
if right.button("Create New Account", use_container_width=True):
  st.write("create new account")

