
import pandas as pd
import mysql.connector

# Railway MySQL connection details
connection = mysql.connector.connect(
    host=st.secrets["mysql"]["host"],
    port=st.secrets["mysql"]["port"],
    user=st.secrets["mysql"]["user"],
    password=st.secrets["mysql"]["password"],
    database=st.secrets["mysql"]["database"],
    ssl_disabled=False
)

df = pd.read_csv("dataset/weather_data.csv")

cursor = connection.cursor()

query = """
INSERT INTO weather (
    weather_date, city, temperature, humidity,
    rainfall, wind_speed, weather_condition
)
VALUES (%s, %s, %s, %s, %s, %s, %s)
"""

for _, row in df.iterrows():
    cursor.execute(query, (
        row["date"],
        row["city"],
        row["temperature"],
        row["humidity"],
        row["rainfall"],
        row["wind_speed"],
        row["weather_condition"]
    ))

connection.commit()

print("Records imported:", cursor.rowcount)

cursor.close()
connection.close()
