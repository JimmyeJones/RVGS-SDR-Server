import streamlit as st
col1, col2, col3 = st.columns(3)
col1.image("RVGSBanner.webp")
col1.write('''<p style="font-size:15px;">Roanoke Valley Governor's School</p>''', unsafe_allow_html=True)
col3.write('<p style="font-size:25px;">Software Defined Radio Server</p>', unsafe_allow_html=True)

col1, col2, col3, col4 = st.columns(4)
if col1.button("Home", width="stretch"):
  page = "home"
if col2.button("Connect", width="stretch"):
  page = "connect"
if col3.button("Satellite Viewer", width="stretch"):
  page = "image_viewer"
if col4.button("About", width="stretch"):
  page = "about"
try:
  str(page)
except NameError:
  page = "home"
st.text(page)
def homepage():
  st.subheader("Roanoke Valley Governor's School")
def connect():
  st.title("Connect")
def image_viewer():
  st.title("Satellite Image Viewer")

