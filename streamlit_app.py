import streamlit as st
import pandas as pd

# --- Page Config ---
st.set_page_config(page_title="Bangalore Restaurants Dashboard", layout="wide")

st.title("🍴 Bangalore Restaurants Dashboard")
st.markdown("Insights from cleaned dataset exported from Databricks")

# --- Load Data ---
tophot = pd.read_csv("data/tophot.csv")
vegvsnonveg = pd.read_csv("data/vegvsnonveg.csv")
toparea = pd.read_csv("data/toparea.csv")
mpd = pd.read_csv("data/mpd.csv")
top10C = pd.read_csv("data/top10C.csv")
keralarest = pd.read_csv("data/keralarest.csv")

# --- Sidebar Dropdown for Navigation ---
st.sidebar.header("📊 Select KPI to View")
option = st.sidebar.selectbox(
    "Choose a dashboard section:",
    [
        "🏆 Top Restaurants / Hotels",
        "🥗 Veg vs 🍗 Non-Veg Restaurants",
        "📍 Top Areas for Restaurants",
        "🍛 Most Popular Dishes",
        "🍜 Top 10 Cuisines",
        "🌴 Kerala Restaurants in Bangalore"
    ]
)

# --- Section Display based on Selection ---
if option == "🏆 Top Restaurants / Hotels":
    st.subheader("🏆 Top Restaurants / Hotels")
    st.dataframe(tophot)

elif option == "🥗 Veg vs 🍗 Non-Veg Restaurants":
    st.subheader("🥗 Veg vs 🍗 Non-Veg Restaurants")
    st.bar_chart(vegvsnonveg.set_index(vegvsnonveg.columns[0]))

elif option == "📍 Top Areas for Restaurants":
    st.subheader("📍 Top Areas for Restaurants")
    st.bar_chart(toparea.set_index(toparea.columns[0]))

elif option == "🍛 Most Popular Dishes":
    st.subheader("🍛 Most Popular Dishes (Pie Chart)")
    # Convert Most Popular Dishes into a pie chart
    import matplotlib.pyplot as plt

    dish_counts = mpd.set_index(mpd.columns[0])
    fig, ax = plt.subplots()
    ax.pie(
        dish_counts.iloc[:, 0], 
        labels=dish_counts.index, 
        autopct='%1.1f%%', 
        startangle=90
    )
    ax.axis("equal")
    st.pyplot(fig)

elif option == "🍜 Top 10 Cuisines":
    st.subheader("🍜 Top 10 Cuisines")
    st.bar_chart(top10C.set_index(top10C.columns[0]))

elif option == "🌴 Kerala Restaurants in Bangalore":
    st.subheader("🌴 Kerala Restaurants in Bangalore")
    st.dataframe(keralarest)

st.markdown("---")
st.caption("Built with ❤️ using Streamlit & Databricks ETL")

