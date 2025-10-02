import streamlit as st
col1, col2, col3 = st.columns(3)
col1.image("RVGSBanner.webp", caption="Roanoke Valley Governor's School")
col3.write('<p style="font-size:25px;">Software Defined Radio Server</p>', unsafe_allow_html=True)

if 'page' not in st.session_state:
    st.session_state['page'] = 'home'

col1, col2, col3, col4 = st.columns(4)
if col1.button("Home", width="stretch"):
  st.session_state['page'] = 'home'
if col2.button("Connect", width="stretch"):
  st.session_state['page'] = 'connect'
col3.link_button("Satellite Viewer", "https://sdr.jalbert.app", width="stretch")
if col4.button("About", width="stretch"):
  st.session_state['page'] = 'about'

st.text(st.session_state['page'])
st.button("test")
def homepage():
  st.subheader("Welcome to the RVGS SDR Server Site!")
def connect():
  st.title("Connect to an SDR")
def about():
  st.title("About this site")

if st.session_state['page'] == 'home':
    homepage()
elif st.session_state['page'] == 'connect':
    connect()
elif st.session_state['page'] == 'about':
    about()
