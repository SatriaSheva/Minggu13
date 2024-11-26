import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Remove the sidebar by collapsing it
st.set_page_config(page_title="Car Price Analysis", layout="wide", initial_sidebar_state="collapsed")

# Menyiapkan dataset dan gambar
dataset_path = "08.csv"  # Ganti dengan path ke file dataset Anda
image_path = "08.png"  # Ganti dengan path ke file gambar Anda

# Sidebar menu
st.sidebar.title("Select Page")
page = st.sidebar.selectbox("Menu", ["Home"])

# Membaca dataset
df = pd.read_csv(dataset_path)

# Halaman Home
st.title("Welcome to Car Price Analysis")
st.image(image_path, caption="Car Price Analysis", use_container_width=True)

# Menambahkan deskripsi
st.write("""
    Welcome to the Car Price Analysis App! 🚗📊

    This app helps you explore and analyze car prices from different brands and models. 
    You can gain insights from the dataset, visualize trends, and much more.

    Use the sidebar to navigate through the app and explore other features in the future.
""")

# Optional: Display basic information about the dataset
st.write("Here is a snapshot of the dataset you're analyzing:")

# Display a preview of the dataset (first few rows)
st.dataframe(df.head())  # Show the first 5 rows of the dataset

# Optional: Basic statistics
st.write("Basic Statistics for the Dataset:")
st.write(df.describe())  # Show basic statistical information of the dataset

# Visualisasi Grafik: Distribusi harga mobil
st.subheader("Car Price Distribution")
fig, ax = plt.subplots(figsize=(10, 6))
ax.hist(df['price'], bins=20, color='skyblue', edgecolor='black')
ax.set_title("Distribution of Car Prices")
ax.set_xlabel("Price")
ax.set_ylabel("Frequency")
st.pyplot(fig)

# Visualisasi Grafik: Rata-rata harga per merk mobil
st.subheader("Average Price by Car Brand")
avg_price = df.groupby("CarName")["price"].mean().sort_values(ascending=False)

fig, ax = plt.subplots(figsize=(10, 6))
avg_price.plot(kind="bar", ax=ax, color="skyblue")
ax.set_title("Average Price by Car Brand")
ax.set_xlabel("Car Brand")
ax.set_ylabel("Average Price")
st.pyplot(fig)
