# 🍽️ Bangalore Restaurants ETL & Dashboard

This project demonstrates a **mini Data Engineering pipeline + analytics dashboard** built using **Databricks (ETL)** and **Streamlit (dashboard)**.  
The dataset contains restaurant details in Bangalore, India (sourced from Zomato), cleaned and aggregated into meaningful **KPIs** for restaurant insights.  

---

## 🎯 Project Goal
- Build an **ETL pipeline** on Databricks to clean and preprocess raw restaurant data.  
- Export **aggregated CSVs** of key metrics (KPIs).  
- Build a **Streamlit dashboard** to visualize insights in an interactive way.  

---

## 📊 Key KPIs & Insights
1. 🏆 **Top Restaurants / Hotels** – Ranked by average cost  
2. 📍 **Top Areas for Restaurants** – Hotspots for dining in Bangalore  
3. 🥗 vs 🍗 **Veg vs Non-Veg Restaurants** – Count and distribution  
4. 🍛 **Most Popular Dishes** – Pie chart of commonly mentioned dishes  
5. 🍜 **Top 10 Cuisines** – Most loved cuisines in Bangalore  
6. 🌴 **Kerala Restaurants in Bangalore** – With address, cost, and cuisines  

---

## 📂 Project Structure
├── data/ # Aggregated CSV files exported from Databricks
│ ├── keralarest.csv # Kerala restaurants in Bangalore
│ ├── mpd.csv # Most popular dishes data
│ ├── top10C.csv # Top 10 cuisines
│ ├── toparea.csv # Top areas for restaurants
│ ├── tophot.csv # Top restaurants / hotels
│ └── vegvsnonveg.csv # Veg vs Non-Veg restaurant split
│
├── streamlit_app.py # Main Streamlit dashboard script
├── requirements.txt # Python dependencies
├── run.vbs # Windows shortcut script to launch Streamlit
└── README.md # Project documentation (this file)


## 🚀 How to Run the Project

1. **Clone the repository**
   ```bash
   git clone https://github.com/<your-username>/<your-repo-name>.git
   cd <your-repo-name>

