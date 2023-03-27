import pandas as pd
import requests

msp_url= 'https://www.ncei.noaa.gov/data/normals-hourly/1991-2020/access/USW00014922.csv'


response = requests.get(msp_url)
response

msp_wind= pd.read_csv(msp_url, usecols=
               ['STATION', 'LATITUDE', 'LONGITUDE', 'DATE', 'month', 'day', 'hour', 'HLY-WIND-AVGSPD', 'HLY-WIND-VCTDIR'])

msp_wind

# rename the 'old_name' column to 'new_name'
msp_wind = msp_wind.rename(columns={'month': 'MONTH', 'hour':'HOUR', 'day':'DAY', 'HLY-WIND-AVGSPD':'HLY_WIND_AVGSPD', 'HLY-WIND-VCTDIR':'HLY_WIND_VCDIR'})
msp_wind

# Define a function to check if wind speed is between 0 and 100
def check_range(value):
    if value >= 0 and value <= 100:
        return 0
    else:
        return 1
    
msp_wind['ERROR_WINDSPD'] = msp_wind['HLY_WIND_AVGSPD'].apply(check_range)

print(msp_wind)

#define a function to check if wind direction is between 0 and 360
def check_range(value):
    if value >= 0 and value <=360:
        return 0
    else:
        return 1

msp_wind['ERROR_WINDVCTR'] = msp_wind['HLY_WIND_VCDIR'].apply(check_range)

print(msp_wind)

#making a new column with wind intensity
def check_range(value):
    if value >= 0 and value <=10:
        return 1
    if value >10 and value <=20:
        return 2
    if value >20 and value <=30:
        return 3
    if value >30 and value <=100:
        return 4
    else:
        return 0

msp_wind['WIND_INTENSITY'] = msp_wind['HLY_WIND_AVGSPD'].apply(check_range)

print(msp_wind)

#making a column with categories for wind direction

def check_range(value):
    if value >= 0 and value <=45:
        return 1
    if value >45 and value <=90:
        return 2
    if value >90 and value <=135:
        return 3
    if value >135 and value <=180:
        return 4
    if value >180 and value <=225:
        return 5
    if value >225 and value <=270:
        return 6
    if value >270 and value <=315:
        return 7
    if value >315 and value <=360:
        return 8
    else:
        return 0

msp_wind['WIND_VCT_CATEGORY'] = msp_wind['HLY_WIND_VCDIR'].apply(check_range)

print(msp_wind)

print(msp_wind.columns)

print(msp_wind.dtypes)

!pip install psycopg2
import psycopg2
print(psycopg2.__version__)






# convert the latitude and longitude columns to WKT
msp_wind['WKT'] = 'POINT (' + msp_wind['LONGITUDE'].astype(str) + ' ' + msp_wind['LATITUDE'].astype(str) + ')'

# print the dataframe
print(msp_wind)

# Convert the 'date' column to a standard format
msp_wind['DATE'] = pd.to_datetime(msp_wind['DATE'], format='%m-%dT%H:%M:%S')

# Print the resulting DataFrame
print(msp_wind)

# Connect to the database
conn = psycopg2.connect(
    host="34.171.172.42",
    port="5432",
    database="postgres",
    user="postgres",
    password=""
)
cur = conn.cursor()

print('connection successful')

# iterate over the dataframe and insert each row into the database using a SQL INSERT statement
for index, row in msp_wind.iterrows():
    cur.execute('''
    INSERT INTO WIND_HISTORIC (STATION, LATITUDE, LONGITUDE, DATE, MONTH, DAY, HOUR, HLY_WIND_AVGSPD, HLY_WIND_VCDIR, ERROR_WINDSPD, ERROR_WINDVCTR, WIND_INTENSITY, WIND_VCT_CATEGORY, WKT) 
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s) 
    ''', (row['STATION'], row['LATITUDE'], row['LONGITUDE'], row['DATE'], row['MONTH'], row['DAY'], row['HOUR'], row['HLY_WIND_AVGSPD'], row['HLY_WIND_VCDIR'], row['ERROR_WINDSPD'], row['ERROR_WINDVCTR'], row['WIND_INTENSITY'], row['WIND_VCT_CATEGORY'], row['WKT']))

# commit the changes to the database and close the cursor and connection
conn.commit()
cur.close()
conn.close()

print('changes committed')




