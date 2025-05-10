import streamlit as st
import pandas as pd 
import plotly.express as px
import json 
import os 
 
st.set_page_config(page_title="Finance App", page_icon="📊", layout="wide")

category_file = "categories.json"

if "categories" not in st.session_state:
    st.session_state.categories = {
        "Uncategorized" : []
    }
    
if os.path.exists(category_file):
    with open(category_file, "r") as f:
        st.session_state.categories = json.load(f) 

def save_categories():
    with open(category_file, "w") as f:
        json.dump(st.session_state.categories, f)
    
def load_transactions(file):
    try:
        df = pd.read_csv(file)
        df.columns = [col.strip() for col in df.columns]
        df["Amount"] = df["Amount"].str.replace(",", "").astype(float)
        df["Date"] = pd.to_datetimeD(df["Date"], format ="%d %b %Y")
        return df 
    
    except Exception as e:
        st.error(f"Error processing file: {str(e)}")
        return None

# File uploading

def main():
    st.title("Finance Dashboard")

    uploaded_file = st.file_uploader("Upload your trasaction CSV file", type=["CSV"])
    # uploaded_file_PDF = st.file_uploader("Upload your transaction PDF file", type=["PDF"])
    
    if uploaded_file is not None:
        df = load_transactions(uploaded_file)
        
        if df is not None:
            debits_df = df[df["Debit/Credit"] == "Debit"].copy() 
            credits_df = df[df["Debit/Credit"] == "Credit"].copy() 
            
            tab1, tab2 = st.tabs(["Expenses (Debits)", "Payments (Credits)"])
            with tab1:
                st.write(debits_df)
                
            with tab2:
                st.write(credits_df)

    # if uploaded_file_PDF is not None:
    #     df = load_transactions(uploaded_file_PDF)
        
main()
    