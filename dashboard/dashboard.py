import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st


sns.set(style='dark')

def create_season_df(df: pd.DataFrame) -> pd.DataFrame:
    season_df = dataset_df.groupby('season').agg({
    'count': 'sum'
    }).sort_values(by='count', ascending=False)

    return season_df


def create_monthly_df(df: pd.DataFrame) -> pd.DataFrame:
    monthly_df = dataset_df.resample(rule='M', on='date').agg({
    'date': 'max',
    'count': 'sum'
    })

    return monthly_df

#Load Dataset
dataset_df = pd.read_csv("bike_day_df.csv")
dataset_df["date"] = pd.to_datetime(dataset_df["date"])

st.header(":sparkles: BIKE SHARING ANALYSIS :sparkles:" )

#Sewa Sepeda Berdasarakan Musim
season_df = create_season_df(dataset_df)
st.subheader("Season Demographics")

col1, col2 = st.columns(2)

with col1:
    fig, ax = plt.subplots(figsize=(18, 9))

    colors = ["#B4E4FF", "#B4E4FF", "#279EFF", "#B4E4FF"]

    sns.barplot(
        y="count",
        x="season",
        data=season_df,
        palette=colors,
        ax=ax
    )
    ax.set_title("The Highest", fontsize=36)
    ax.set_ylabel(None)
    ax.set_xlabel("Season : (1) Spring (2) Summer (3) Fall (4) Winter", fontsize=30)
    ax.tick_params(axis='x', labelsize=35)
    ax.tick_params(axis='y', labelsize=30)
    st.pyplot(fig)

with col2:
    fig, ax = plt.subplots(figsize=(18, 9))

    colors = ["#279EFF", "#B4E4FF", "#B4E4FF", "#B4E4FF"]

    sns.barplot(
        y="count",
        x="season",
        data=season_df,
        palette=colors,
        ax=ax
    )
    ax.set_title("The Lowest", fontsize=36)
    ax.set_ylabel(None)
    ax.set_xlabel("Season : (1) Spring (2) Summer (3) Fall (4) Winter", fontsize=30)
    ax.tick_params(axis='x', labelsize=35)
    ax.tick_params(axis='y', labelsize=30)
    st.pyplot(fig)

with st.expander("Penjelasan"):
    st.write(
        """
        Berdasarkan diagram batang diatas dapat disimpulkan bahwa jumlah
        penyewaan sepeda tertinggi/terbanyak terjadi pada musim Fall (Gugur)
        sedangkan jumlah penyewaan sepeda terendah/sedikit terjadi pada musim Spring (Semi).
        """
    )

#Perkembangan Sewa Sepeda
monthly_df = create_monthly_df(dataset_df)
st.subheader("Bike Rental Trends 2011-2012")

fig, ax = plt.subplots(figsize=(10, 4))
ax.plot(
    monthly_df['date'],
    monthly_df['count'],
    marker='o',
    color="#0C356A"
)

ax.set_title("Bike Rental 2011-2012")

st.pyplot(fig)

with st.expander("Penjelasan"):
    st.write(
        """
        Sepanjang tahun 2011 sampai dengan 2012 penyewaan sepeda mengalami kenaikan dan penurunan.
        Kenaikan terjadi pada awal tahun 2011 sampai Juli 2011 namun terjadi penurunan sampai bulan Desember 2011.
        Memasuki awal tahun 2012 sewa sepeda mengalami kenaikan lagi sampai bulan Oktober tetapi kembali lagi mengalami penurunan hingga akhir tahun 2012.
        """
    )

st.caption('Copyright (c) 2023')

