import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Interactive Streamlit elements, like these sliders, return their value.
# This gives you an extremely simple interaction model.
faces = st.sidebar.slider("ダイスの面数", 4, 20, 6, 1)
num = st.sidebar.slider("何個振ったか", 1, 100, 1, 1)
trials = st.sidebar.slider("試行回数", 10, 10000, 100, 10)

l = []
for i in range(trials):
    data = np.random.randint(1, faces + 1, num)
    l.append(np.sum(data) / num)

st.text(str(l))
# # test 用の出目の和の個数チェッカー
# l2 = [0] * (faces * num + 1)
# for i in l:
#     l2[i] += 1
# for i, d in enumerate(l2):
#     if i == 0:
#         continue
#     st.text(str(i) + ": " + str(d) + "個")

# グラフ設定
fig = plt.figure(figsize=(20,10))
st.subheader('サイコロの和の平均値の分布')
sns.distplot(l)
st.pyplot(fig)
