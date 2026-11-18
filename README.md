# 🌦️ Weather Data Analysis Dashboard

A web-based dashboard for exploring and analyzing weather records from different cities. The application is built with **Python, Streamlit, Pandas, and MySQL**.

## 🚀 Live Demo

[Open the Weather Analysis Dashboard](https://deepika-20061103-weather-analysis-dashboard-piaofg.streamlit.app/)

## 📌 Project Repository

[View the source code on GitHub](https://github.com/Deepika-20061103/weather_analysis)

## ✨ Features

- **Weather overview:** View the total number of records, average temperature, maximum temperature, and total rainfall.
- **City-wise analysis:** Compare average temperatures and rainfall across cities.
- **Weather condition distribution:** Explore the number of records for each weather condition.
- **Interactive filters:** Filter records by city, weather condition, and date range.
- **Weather records:** View the filtered results in an interactive data table.
- **CSV export:** Download the filtered weather data.
- **Automatic insights:** Identify the hottest city, the city with the highest total rainfall, and the number of rainy records.

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Application development |
| Streamlit | Interactive dashboard and web interface |
| Pandas | Data loading, cleaning, filtering, and analysis |
| MySQL | Weather data storage |
| mysql-connector-python | Python–MySQL connectivity |

## 📂 Project Structure

```text
weather_analysis/
├── dataset/                 # Weather dataset
├── queries/                 # SQL queries
├── .devcontainer/           # Development container configuration
├── dashboard.py             # Streamlit dashboard application
├── import_to_railway.py     # Script for importing weather data
├── requirements.txt         # Python dependencies
└── README.md                # Project documentation
```

## ⚙️ Run the Project Locally

### 1. Clone the repository

```bash
git clone https://github.com/Deepika-20061103/weather_analysis.git
cd weather_analysis
```

### 2. Create and activate a virtual environment

**macOS / Linux**
```bash
python3 -m venv venv
source venv/bin/activate
```

**Windows**
```bash
python -m venv venv
venv\\Scripts\\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Prepare the MySQL database

Create a MySQL database named `weather_db` and a table named `weather` with the columns used by the dashboard:

```sql
CREATE DATABASE weather_db;
USE weather_db;

CREATE TABLE weather (
    weather_date DATE,
    city VARCHAR(100),
    temperature FLOAT,
    humidity FLOAT,
    rainfall FLOAT,
    wind_speed FLOAT,
    weather_condition VARCHAR(100)
);
```

Load your weather records into the `weather` table. Make sure your MySQL server is running.

### 5. Start the dashboard

```bash
streamlit run dashboard.py
```

Open the local URL displayed in your terminal (usually `http://localhost:8501`). Enter your MySQL username and password in the dashboard sidebar and select **Connect to MySQL**.

> **Note:** The dashboard code connects to a MySQL server at `localhost` and uses the `weather_db` database. For local execution, configure the database and table accordingly.

## 📊 Dashboard Workflow

1. Connect the dashboard to the MySQL database.
2. Retrieve weather records using SQL.
3. Analyze the data with Pandas.
4. Display summary metrics, charts, and automatic insights.
5. Filter records and export the selected data as a CSV file.

## 🎯 Project Objective

The objective of this project is to demonstrate how weather data stored in a relational database can be queried, analyzed, and presented through an interactive dashboard. It helps users explore weather patterns across cities using visual summaries and filters.

## 👩‍💻 Author

**Deepika Devi**

- GitHub: [Deepika-20061103](https://github.com/Deepika-20061103)
- Project: [Weather Analysis](https://github.com/Deepika-20061103/weather_analysis)
- Live Demo: [Weather Analysis Dashboard](https://deepika-20061103-weather-analysis-dashboard-piaofg.streamlit.app/)
