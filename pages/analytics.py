import streamlit as st
import pandas as pd
import plotly.express as px

st.title("📊 Analytics Dashboard")

try:

    df = pd.read_csv(
        "data/translation_history.csv"
    )

    st.dataframe(df)

    chart = px.histogram(
        df,
        x="Target",
        title="Target Languages Usage"
    )

    st.plotly_chart(
        chart,
        use_container_width=True
    )

except:
    st.warning("No data available")