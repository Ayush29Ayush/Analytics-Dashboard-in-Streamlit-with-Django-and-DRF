import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

st.title("Analytics Dashboard")
st.write("Version 0.1")

#! Test Chart
categories = ["A", "B", "C", "D"]
values = np.random.randint(low=10, high=100, size=4)

fig, ax = plt.subplots()
ax.bar(categories, values, color="blue")
ax.set_xlabel("Categories")
ax.set_ylabel("Values")
ax.set_title("Bar Chart")
st.plotly_chart(fig)
