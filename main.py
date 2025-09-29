import streamlit as st
st.title("Software Defined Radio Server")
col1, col2, col3, col4 = st.columns(4)
if col1.button("Home", width="stretch"):
  page = "home"
if col2.button("Connect", width="stretch"):
  page = "connect"
if col3.button("Satellite Viewer"):
  page = "image_viewer"
if col4.button("About", width="stretch"):
  page = "about"
def homepage():
  st.subheader("Roanoke Valley Governor's School")
def connect():
  st.title("Connect")
def image_viewer():
  st.title("Satellite Image Viewer")

