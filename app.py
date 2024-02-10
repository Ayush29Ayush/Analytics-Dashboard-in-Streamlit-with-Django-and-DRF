import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import altair as alt
import pandas as pd
import requests

#! Endpoints
swapi_endpoint = "https://swapi.dev/api/people/1/"
api_url = "http://127.0.0.1:8000/api/customers/"

#! Functions
def fetch_data(endpoint):
    response = requests.get(endpoint)
    data = response.json()
    return data

def send_data(name, gender, age, favorite_number):
    gender_value = "0" if gender == "Female" else "1"
    
    data = {
        "name": name,
        "gender": gender_value,
        "age": age,
        "favorite_number": favorite_number
    }
    
    response = requests.post(api_url, json=data)
    return response 

st.title("Analytics Dashboard")
st.write("Version 0.1")

#! Layout customization
col1, col2 = st.columns(2)

with col1:
    st.header("First Column")
    st.write("This is the first column")
    
    with st.expander("Click to choose something"):
        st.write("option to choose")
        st.write("another option to choose")
        
with col2:
    #! Test Chart
    categories = ["A", "B", "C", "D"]
    values = np.random.randint(low=10, high=100, size=4)

    fig, ax = plt.subplots()
    ax.bar(categories, values, color="blue")
    ax.set_xlabel("Categories")
    ax.set_ylabel("Values")
    ax.set_title("Bar Chart")
    # st.plotly_chart(fig)
    st.pyplot(fig)

#! Session state
if 'counter' not in st.session_state:
    st.session_state.counter = 0
    
#! Increment button
if st.button("Increment"):
    st.session_state.counter += 1
    
st.write(f"You clicked {st.session_state.counter} times")

#! Data from SWAPI API
# swapi_endpoint = "https://swapi.dev/api/people/1/"

swapi_data = fetch_data(swapi_endpoint)

st.write('Data from SWAPI API:')
st.json(swapi_data)

#! Fetch data from our API
# api_url = "http://127.0.0.1:8000/api/customers/"
data = fetch_data(api_url)

if data:
    df = pd.DataFrame(data)
    
    st.dataframe(df)
    
    scatter_chart = alt.Chart(df).mark_circle(size=60).encode(
        x='age',
        y='favorite_number',
    )
    
    st.altair_chart(scatter_chart, use_container_width=True)
    
# Form to collect customer data
name = st.text_input("Name")
gender = st.radio("Select your gender", ["Male", "Female"])
age = st.slider("Select your age", 1, 100, 18)
favorite_number = st.number_input("Favorite number", step=1)

if st.button("Submit"):
    response = send_data(name, gender, age, favorite_number)

    if response.status_code == 201:
        st.success("Data submitted successfully")
        st.rerun()
    else:
        st.error("Error submitting data")