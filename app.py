import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Nassau Candy Factory Optimization",
    page_icon="🏭",
    layout="wide"
)

st.title("🏭 Nassau Candy Factory Reallocation")
st.subheader("Shipping Optimization Recommendation System")

st.write(
    "An interactive analytics dashboard for exploring "
    "factory allocation, shipping performance, and profitability."
)

st.divider()

st.header("📊 Project Overview")

col1, col2, col3 = st.columns(3)

col1.metric("Factories", "5")
col2.metric("Project Type", "Machine Learning")
col3.metric("Objective", "Shipping Optimization")

st.divider()

st.header("🏭 Factory Information")

factories = [
    "Lot's O' Nuts",
    "Wicked Choccy's",
    "Sugar Shack",
    "Secret Factory",
    "The Other Factory"
]

selected_factory = st.selectbox(
    "Select a factory",
    factories
)

st.write("**Selected Factory:**", selected_factory)

st.info(
    "This application supports factory allocation analysis "
    "and shipping optimization research."
)

st.caption(
    "Project: Nassau Candy Distributor | Developed using Python and Streamlit"
)
