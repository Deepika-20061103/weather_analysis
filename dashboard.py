
import streamlit as st
import pandas as pd
import mysql.connector

# -----------------------------------
# 1. PAGE CONFIGURATION
# -----------------------------------

st.set_page_config(
    page_title="Weather Analysis Dashboard",
    page_icon="🌦️",
    layout="wide"
)

# -----------------------------------
# 2. DASHBOARD TITLE
# -----------------------------------

st.title("🌦️ Weather Data Analysis Dashboard")

st.markdown("""
### Weather Data Processing and Analysis Using MySQL

This dashboard analyzes weather information
collected from different cities.
""")

st.divider()

# -----------------------------------
# 3. CONNECT TO RAILWAY MYSQL
# -----------------------------------

@st.cache_data(ttl=300)
def load_weather_data():

    connection = mysql.connector.connect(
    host=st.secrets["mysql"]["host"],
    port=int(st.secrets["mysql"]["port"]),
    user=st.secrets["mysql"]["user"],
    password=st.secrets["mysql"]["password"],
    database=st.secrets["mysql"]["database"],
    ssl_disabled=False
)

    cursor = connection.cursor(dictionary=True)

    try:
        query = """
            SELECT weather_date, city, temperature,
                   humidity, rainfall, wind_speed,
                   weather_condition
            FROM weather
            ORDER BY weather_date, city
        """

        cursor.execute(query)
        rows = cursor.fetchall()

        # Build the DataFrame directly from MySQL results.
        # This avoids pandas' DBAPI connection compatibility warning.
        df = pd.DataFrame(rows)

    finally:
        cursor.close()
        connection.close()

    return df


# -----------------------------------
# 4. LOAD WEATHER DATA
# -----------------------------------

try:
    with st.spinner("Connecting to Railway MySQL..."):
        df = load_weather_data()

    st.success("Connected to Railway MySQL successfully!")

except Exception as error:
    st.error("Unable to connect to the Railway database.")
    st.info(
        "Check your Streamlit Cloud Secrets settings "
        "and Railway database credentials."
    )
    st.stop()

if df.empty:
    st.warning("No weather records found.")
    st.stop()

df["weather_date"] = pd.to_datetime(df["weather_date"])

# -----------------------------------
# 5. WEATHER OVERVIEW
# -----------------------------------

st.subheader("📊 Weather Overview")

col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Records", len(df))

col2.metric(
    "Average Temperature",
    f"{df['temperature'].mean():.2f} °C"
)

col3.metric(
    "Maximum Temperature",
    f"{df['temperature'].max():.1f} °C"
)

col4.metric(
    "Total Rainfall",
    f"{df['rainfall'].sum():.1f} mm"
)

st.divider()

# -----------------------------------
# 6. CITY-WISE TEMPERATURE
# -----------------------------------

st.subheader("🌡️ Average Temperature by City")

city_temp = (
    df.groupby("city")["temperature"]
    .mean()
    .reset_index()
)

st.bar_chart(city_temp, x="city", y="temperature")

# -----------------------------------
# 7. CITY-WISE RAINFALL
# -----------------------------------

st.subheader("🌧️ Average Rainfall by City")

city_rain = (
    df.groupby("city")["rainfall"]
    .mean()
    .reset_index()
)

st.bar_chart(city_rain, x="city", y="rainfall")

st.divider()

# -----------------------------------
# 8. WEATHER CONDITION DISTRIBUTION
# -----------------------------------

st.subheader("☁️ Weather Condition Distribution")

condition_count = (
    df["weather_condition"]
    .value_counts()
    .reset_index()
)

condition_count.columns = ["Weather Condition", "Days"]

st.bar_chart(
    condition_count,
    x="Weather Condition",
    y="Days"
)

st.divider()

# -----------------------------------
# 9. FILTER WEATHER RECORDS
# -----------------------------------

st.subheader("🔎 Explore Weather Records")

col1, col2 = st.columns(2)

with col1:
    selected_city = st.selectbox(
        "Select City",
        ["All"] + sorted(df["city"].dropna().unique().tolist())
    )

with col2:
    selected_condition = st.selectbox(
        "Select Weather Condition",
        ["All"] + sorted(
            df["weather_condition"].dropna().unique().tolist()
        )
    )

filtered_df = df.copy()

if selected_city != "All":
    filtered_df = filtered_df[
        filtered_df["city"] == selected_city
    ]

if selected_condition != "All":
    filtered_df = filtered_df[
        filtered_df["weather_condition"] == selected_condition
    ]

# -----------------------------------
# 10. DATE RANGE FILTER
# -----------------------------------

st.subheader("📅 Filter by Date")

date_range = st.date_input(
    "Select Date Range",
    value=(
        df["weather_date"].min().date(),
        df["weather_date"].max().date()
    ),
    min_value=df["weather_date"].min().date(),
    max_value=df["weather_date"].max().date()
)

if len(date_range) == 2:
    start_date, end_date = date_range

    filtered_df = filtered_df[
        (filtered_df["weather_date"].dt.date >= start_date)
        &
        (filtered_df["weather_date"].dt.date <= end_date)
    ]

# -----------------------------------
# 11. DISPLAY WEATHER RECORDS
# -----------------------------------

st.subheader("📋 Weather Records")

st.write(f"Showing {len(filtered_df)} weather records.")

st.dataframe(
    filtered_df,
    width="stretch",
    hide_index=True
)

# -----------------------------------
# 12. DOWNLOAD CSV
# -----------------------------------

st.subheader("📥 Download Weather Data")

csv_data = filtered_df.to_csv(index=False).encode("utf-8")

st.download_button(
    label="Download Weather Data as CSV",
    data=csv_data,
    file_name="weather_analysis.csv",
    mime="text/csv"
)

st.divider()

# -----------------------------------
# 13. AUTOMATIC WEATHER INSIGHTS
# -----------------------------------

st.subheader("💡 Weather Insights")

hottest_city = (
    df.groupby("city")["temperature"]
    .mean()
    .idxmax()
)

highest_rainfall_city = (
    df.groupby("city")["rainfall"]
    .sum()
    .idxmax()
)

rainy_days = (
    df["weather_condition"]
    .str.lower() == "rainy"
).sum()

st.write(f"🌡️ **Hottest city:** {hottest_city}")
st.write(f"🌧️ **Highest total rainfall:** {highest_rainfall_city}")
st.write(f"☔ **Total rainy records:** {rainy_days}")

st.success("Weather data analysis completed successfully!")

# -----------------------------------
# 14. FOOTER
# -----------------------------------

st.divider()

st.caption(
    "Weather Data Processing and Analysis Using MySQL | "
    "Developed using Python, Streamlit and MySQL"
)
