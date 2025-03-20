import streamlit as st
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier

st.title('🤖 e-commerce App')

st.info('This is a EDA app!')

with st.expander('Data'):
  st.write('**Raw data**')
  df = pd.read_csv("https://raw.githubusercontent.com/fay-55/Portofolio_streamlit2/main/ecommerce_cleaned.csv")

  st.dataframe(df)  # Lebih interaktif dan bisa discroll

 # Konversi ke datetime
df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'], errors='coerce')
    
    # Hapus data yang tidak valid
df = df.dropna(subset=['InvoiceDate'])

    # Cek apakah perubahan terjadi
st.write(df['InvoiceDate'].head())

df['Sales'] = df['Quantity'] * df['UnitPrice']  # Hitung total penjualan

df_grouped = df.groupby(df['InvoiceDate'].dt.date)['Sales'].sum().reset_index()
df_grouped.columns = ['Date', 'Total Sales']

st.dataframe(df_grouped)  # Lihat hasilnya

with st.expander('📈 Data Visualization'):
    st.line_chart(df_grouped.set_index('Date'))

st.selectbox("Pilih negara", df['Country'].unique())
selected_products = st.multiselect("Pilih Produk", df['Description'].unique())
if selected_products:
    filtered_df = df[df['Description'].isin(selected_products)]
    st.dataframe(filtered_df)

st.slider("Range harga", float(df['UnitPrice'].min()),
float(df['UnitPrice'].max()), (float(df['UnitPrice'].min()), float(df['UnitPrice'].max())))

st.selectbox("Pilih Hari", df['DayName'].unique())

df['Quantity'] = pd.to_numeric(df['Quantity'], errors='coerce')
df['Quantity'] = df['Quantity'].fillna(0).astype(int)

st.slider("📦 Pilih Rentang Quantity", 
                           int(df["Quantity"].min()), 
                           int(df["Quantity"].max()), 
                           (int(df["Quantity"].min()), int(df["Quantity"].max())))

search_term = st.text_input("Cari Produk")
if search_term:
    search_results = df[df['Description'].str.contains(search_term, case=False, na=False)]
    st.dataframe(search_results)


# filterd_df = df[(df['Country'] == country) & 
#(df['DayName'] == day_selected) &
#(df['UnitPrice'] >= min_price) & (df['UnitPrice'] <= max_price) &
#(df['Quantity'] >= quatity_range[0]) & (df['Quantity'] <= quatity_range[1])]

#st.dataframe(filterd_df)