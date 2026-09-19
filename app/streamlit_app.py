import streamlit as st
import pandas as pd
import plotly.express as px
st.set_page_config(page_title="Project FORESIGHT",layout="wide")
st.title("Project FORESIGHT — Demand & Inventory Intelligence")
@st.cache_data
def load():
    return pd.read_excel("data/Project_FORESIGHT_Complete_Submission.xlsx",sheet_name="Raw_Data")
df=load()
c1,c2,c3,c4=st.columns(4)
c1.metric("Revenue",f"₹{df.Revenue.sum()/1e7:.2f} Cr")
c2.metric("Demand",f"{df.Demand_Units.sum():,.0f}")
c3.metric("Stockout records",f"{df.Stockout_Flag.sum():,.0f}")
c4.metric("Overstock records",f"{df.Overstock_Flag.sum():,.0f}")
a,b=st.columns(2)
with a: st.plotly_chart(px.bar(df.groupby("Category",as_index=False).Revenue.sum(),x="Category",y="Revenue",title="Revenue by Category"),use_container_width=True)
with b:
    r=df.Risk_Level.value_counts().reset_index(); r.columns=["Risk_Level","Count"]
    st.plotly_chart(px.bar(r,x="Risk_Level",y="Count",title="Risk Distribution"),use_container_width=True)
st.subheader("Planning Data")
st.dataframe(df.head(300),use_container_width=True)
