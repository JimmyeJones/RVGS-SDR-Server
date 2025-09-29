import streamlit as st
st.title("Software Defined Radio Server")
col1, col2, col3, col4 = st.columns(4)
if col1.button("Home                   "):
  page = "home"
if col2.button("Connect                "):
  page = "connect"
if col3.button("Satellite Image Viewer"):
  page = "image_viewer"
if col4.button("About                 "):
  page = "about"
def homepage():
  st.subheader("Roanoke Valley Governor's School")
def connect():
  st.title("Connect")
def image_viewer():
  st.title("Satellite Image Viewer")

