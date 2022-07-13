import streamlit as st
import numpy as np

n=np.random.permutation(8)

st.subheader('Chose 1')
st.text(n)

