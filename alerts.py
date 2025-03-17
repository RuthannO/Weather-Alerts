import requests
import psycopg2
import pymongo as MongoClient
import datetime
from dotenv import load_dotenv
import os

url = "https://api.weather.gov/alerts/active"
response = requests.get(url)
data = response.json()

load_dotenv()

pg_pwd = os.getenv('PG_PASSWORD')
pg_db = os.getenv('PG_DB')
pg_user = os.getenv('PG_USER')

conn = psycopg2.connect(
    dbname = pg_db,
    password = pg_pwd,
    user = pg_user,
    host = 'localhost',
    port = '5432'
)
cursor = conn.cursor()

##TEST THING
#alert = data['features'][0]['properties']
#event_time = alert['sent']
#event = alert['event']
#region = alert['areaDesc']
#severity = alert['severity']
#urgency = alert['urgency']
#
#******************************************


#check the response and processes the data
if response.status_code == 200:
    data = response.json()
#saves and opens in a JSON file
    with open('weather_alerts.json', 'w') as f:
        import json
        json.dump(data, f, indent=4)
    print("Data saved to weather_alerts.json")
    
# Check how many alerts are inside
print(f"Number of alerts found: {len(data['features'])}")

#T
#Transforms the data into something more readable

#This creates an empty list to hold the data
weather_alerts = data['features']

#loop to go through the JSON file and access details about the earthquake, "features" and 'properties' are referenced in the file
for alert in weather_alerts:
    props = alert['properties']
    event_time = props.get('sent')
    event = props.get('event')
    region = props.get('areaDesc')
    severity = props.get('severity','Unknown')
    urgency = props.get('urgency',"Unknown")
    description = props.get('description')
    sender = props.get('senderName')

    print(f"Processing alert for region: {props.get('areaDesc')}")

    print(props.keys())

#**********************************************
    cursor.execute("""
    INSERT INTO weather_alerts (event_time,event, region, severity,urgency,description,sender)
    VALUES (%s, %s, %s, %s,%s,%s,%s)
""", (event_time, region, severity, event, urgency, description, sender))
    conn.commit()

    print(f"✅ Stored: {event} | Severity: {severity}")
cursor.close()
conn.close()