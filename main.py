import streamlit as st
col1, col2, col3 = st.columns(3)
col1.image("RVGSBanner.webp")
col1.write('''<p style="font-size:15px;">Roanoke Valley Governor's School</p>''', unsafe_allow_html=True)
col3.write('<p style="font-size:25px;">Software Defined Radio Server</p>', unsafe_allow_html=True)

if 'page' not in st.session_state:
    st.session_state['page'] = 'home'

col1, col2, col3, col4 = st.columns(4)
if col1.button("Home", width="stretch"):
  st.session_state['page'] = 'home'
if col2.button("Connect", width="stretch"):
  st.session_state['page'] = 'connect'
if col3.button("Satellite Viewer", width="stretch"):
  st.session_state['page'] = 'image_viewer'
if col4.button("About", width="stretch"):
  st.session_state['page'] = 'about'

st.text(st.session_state['page'])
st.button("test")
def homepage():
  st.subheader("Roanoke Valley Governor's School")
def connect():
  st.title("Connect")
def image_viewer():
  st.title("Satellite Image Viewer")

