# app.py
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

# Page config
st.set_page_config(page_title="COVID-19 Dashboard", layout="wide")

# Load data
@st.cache_data
def load_data():
    df = pd.read_csv("owid-covid-data.csv")
    df['date'] = pd.to_datetime(df['date'])
    return df

df = load_data()

# Title
st.title("🌍 COVID-19 Global Data Tracker")

# Country selection
countries = df['location'].unique()
selected_country = st.selectbox("Select a country:", sorted(countries))

# Filter data
country_data = df[df['location'] == selected_country]

# Line chart: Total cases
st.subheader(f"📈 Total Cases Over Time - {selected_country}")
fig, ax = plt.subplots()
ax.plot(country_data['date'], country_data['total_cases'], color='blue')
ax.set_xlabel("Date")
ax.set_ylabel("Total Cases")
ax.set_title(f"COVID-19 Total Cases in {selected_country}")
st.pyplot(fig)

# Line chart: Total deaths
st.subheader(f"💀 Total Deaths Over Time - {selected_country}")
fig, ax = plt.subplots()
ax.plot(country_data['date'], country_data['total_deaths'], color='red')
ax.set_xlabel("Date")
ax.set_ylabel("Total Deaths")
ax.set_title(f"COVID-19 Total Deaths in {selected_country}")
st.pyplot(fig)

# Line chart: Vaccination

if 'total_vaccinations' in country_data.columns:
    st.subheader(f"💉 Vaccinations Over Time - {selected_country}")
    fig, ax = plt.subplots()
    ax.plot(country_data['date'], country_data['total_vaccinations'], color='green')

    # Format x-axis to show only years
    ax.xaxis.set_major_locator(mdates.YearLocator())
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))

    ax.set_xlabel("Year")
    ax.set_ylabel("Total Vaccinations")
    ax.set_title(f"COVID-19 Vaccinations in {selected_country}")
    fig.autofmt_xdate()  # Auto rotate if needed
    st.pyplot(fig)
else:
    st.info("Vaccination data not available for this country.")
