<<<<<<< HEAD
import streamlit as st
import os
import psycopg2 as dbconn
import pandas as pd
from dotenv import load_dotenv

load_dotenv()

conn = dbconn.connect(
    dbname = os.getenv('PG_DB'),
    user = os.getenv('PG_USER'),
    password = os.getenv('PG_PASSWORD'),
    host = 'localhost',
    port = '5432'
)

df = pd.read_sql("SELECT * FROM weather_alerts ORDER BY event_time DESC LIMIT 100", conn)

# Display in Streamlit
st.title("🌦️ Weather Alerts Dashboard")
st.dataframe(df)

# Bar Chart: Alerts by Severity
st.subheader("Alerts by Severity")
severity_counts = df['severity'].value_counts()
st.bar_chart(severity_counts)

conn.close()
=======
import streamlit as st
import os
import psycopg2 as dbconn
import pandas as pd
from dotenv import load_dotenv

load_dotenv()

conn = dbconn.connect(
    dbname = os.getenv('PG_DB'),
    user = os.getenv('PG_USER'),
    password = os.getenv('PG_PASSWORD'),
    host = 'localhost',
    port = '5432'
)

df = pd.read_sql("SELECT * FROM weather_alerts ORDER BY event_time DESC LIMIT 100", conn)

# Display in Streamlit
st.title("🌦️ Weather Alerts Dashboard")
st.dataframe(df)

# Bar Chart: Alerts by Severity
st.subheader("Alerts by Severity")
severity_counts = df['severity'].value_counts()
st.bar_chart(severity_counts)

conn.close()
>>>>>>> 384dee05cb70727df337d3953151861372f81404
