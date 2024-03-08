import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

main_data = pd.read_csv('main_data.csv')


sellers_in_cities = main_data.groupby(by="seller_city").seller_id.nunique().sort_values(ascending=False).reset_index()

st.header("Dashboard E-Commerce Public Dataset")


st.subheader("Produk Paling Laris dan Paling Sepi")
item_data1 = main_data.groupby("product_category_name_english")["product_id"].count().reset_index()
item_data1 = item_data1.sort_values(by="product_id", ascending=False)

plt.figure(figsize=(12, 6))
sns.barplot(x="product_id", y="product_category_name_english", data=item_data1.head(10), color="skyblue", legend=False)


plt.xlabel("Jumlah Produk")
plt.ylabel("Kategori Produk (Bahasa Inggris)")
plt.title("Jumlah Produk Paling Laris")
st.pyplot(plt)

item_data2 = main_data.groupby("product_category_name_english")["product_id"].count().reset_index()
item_data2 = item_data2.sort_values(by="product_id", ascending=True)
item_data2 = item_data2.head(10)  
plt.figure(figsize=(12, 6))
sns.barplot(x="product_id", y="product_category_name_english", data=item_data2, color="skyblue", legend=False)
plt.xlabel("Jumlah Produk")
plt.ylabel("Kategori Produk (Bahasa Inggris)")
plt.title("Jumlah Produk Paling Sepi")
st.pyplot(plt)
st.markdown("Berdasarkan visualisasi di atas, dapat dilihat bahwa bed bath table adalah produk paling laris dan securiy and services adalah produk paling sepi", unsafe_allow_html=True)




st.subheader("Penyebaran Penjual Berdasarkan Kota")
plt.figure(figsize=(12, 6))
sns.barplot(x="seller_id", y="seller_city", data=sellers_in_cities.head(10), color="skyblue")

plt.xlabel("Jumlah Penjual")
plt.ylabel("Kota")
plt.title("Penyebaran Penjual Berdasarkan Kota")

st.pyplot(plt)

st.markdown("Berdasarkan visualisasi di atas, dapat dilihat bahwa Penjual paling banyak berasal dari kota Sao Paulo, Curitiba, dan Rio de Janeiro", unsafe_allow_html=True)
