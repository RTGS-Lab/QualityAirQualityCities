import pandas as pd
import requests

msp_url= 'https://www.ncei.noaa.gov/data/normals-hourly/1991-2020/access/USW00014922.csv'


response = requests.get(msp_url)
response

msp_wind= pd.read_csv(msp_url, usecols=
               ['STATION', 'LATITUDE', 'LONGITUDE', 'DATE', 'month', 'day', 'hour', 'HLY-WIND-AVGSPD', 'HLY-WIND-VCTDIR'])

msp_wind

# Define a function to check if wind speed is between 0 and 100
def check_range(value):
    if value >= 0 and value <= 100:
        return 0
    else:
        return 1
    
msp_wind['error_wndspd'] = msp_wind['HLY-WIND-AVGSPD'].apply(check_range)

print(msp_wind)

#define a function to check if wind direction is between 0 and 360
def check_range(value):
    if value >= 0 and value <=360:
        return 0
    else:
        return 1

msp_wind['error_wnddrctn'] = msp_wind['HLY-WIND-VCTDIR'].apply(check_range)

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

msp_wind['wind_intensity'] = msp_wind['HLY-WIND-AVGSPD'].apply(check_range)

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

msp_wind['wind_category_direction'] = msp_wind['HLY-WIND-VCTDIR'].apply(check_range)

print(msp_wind)




