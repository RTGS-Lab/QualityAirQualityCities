### This script will store all of our Daily Summary Functions
### They will be stored along with statistic names and their value types in iterables

### Storage

summary_stats_names = [] # Stat Names

summary_stats_dtypes = [] # Stat Value Types

summary_stats_functions = [] # The functions


# ~~~~~

### The Functions - These should return the stats as a list (even if it is just one stat)

# ~~~~~

## Number of observations

def n_observations(df):
    
    return [len(df)]

# Add to storage

summary_stats_names += ['n_observations'] # Stat Names

summary_stats_dtypes += [int] # Stat Value Types

summary_stats_functions += [n_observations]

# ~~~~~

## Daily Stats

def pm25_fullDay_stats(df):
    
    stats_list = []
    
    if len(df) == 0:
        
        stats_list = [None]*6
    
    else:
    
        mean = df.pm25.mean()
        min = df.pm25.min()
        mintime = df.loc[df['pm25'].idxmin(), 'timestamp'].time()
        max = df.pm25.max()
        maxtime = df.loc[df['pm25'].idxmax(), 'timestamp'].time()
        std = df.pm25.std()
    
        stats_list = [mean, min, str(mintime), max, str(maxtime), std]
        
    return stats_list

# Add to storage

summary_stats_names += ['pm25_fullDay_mean', 'pm25_fullDay_min', 'pm25_fullDay_minTime',
                        'pm25_fullDay_max', 'pm25_fullDay_maxTime', 'pm25_fullDay_std'] # Stat Names

summary_stats_dtypes += [float, float, str, float, str, float] # Stat Value Types

summary_stats_functions += [pm25_fullDay_stats]

# ~~~~~

## Daily Total Minutes Above 12 micrograms per cubic meter

def daily_minutes_above_12ug(df):
    #convert timestamp to pandas datetime object for comparison

    # Filter rows where pm25 values are above 12
    df_above_12 = df[df['pm25'] > 12]

    # each reading in the new df represents a ten minute average for that time block, so I'll multiply the length of the column by 10 to get the total time in minutes!
    mins_above_12ug = len(df_above_12) * 10
    
    return [mins_above_12ug]

# Add to storage

summary_stats_names += ['pm25_fullDay_minutesAbove12ug'] # Stat Names

summary_stats_dtypes += [int] # Stat Value Types

summary_stats_functions += [daily_minutes_above_12ug]

# ~~~~~

# Morning rush hour statistics

def pm25_morningRush_stats(df):
    
    # Select By time
    
    df_6_to_9 = df.loc[(df['timestamp'].dt.hour >= 6) & (df['timestamp'].dt.hour < 9)]
    
    stats_list = []
    
    if len(df_6_to_9) == 0:
        
        stats_list = [None]*6
    
    else:

        pm25_morningRush_min = df_6_to_9['pm25'].min()
        mintime = df_6_to_9.loc[df_6_to_9['pm25'].idxmin(), 'timestamp'].time()
        pm25_morningRush_max = df_6_to_9['pm25'].max()
        maxtime = df_6_to_9.loc[df_6_to_9['pm25'].idxmax(), 'timestamp'].time()
        pm25_morningRush_mean = df_6_to_9['pm25'].mean()
        pm25_morningRush_std = df_6_to_9['pm25'].std()
        
        stats_list = [pm25_morningRush_mean, pm25_morningRush_min, str(mintime), pm25_morningRush_max, str(maxtime), pm25_morningRush_std]
    
    return stats_list

# Add to storage

summary_stats_names += ['pm25_morningRush_mean', 'pm25_morningRush_min', 'pm25_morningRush_minTime',
                        'pm25_morningRush_max', 'pm25_morningRush_maxTime', 'pm25_morningRush_std'] # Stats Names

summary_stats_dtypes += [float, float, str, float, str, float] # Stat Value Types

summary_stats_functions += [pm25_morningRush_stats]

# ~~~~~

# Evening rush hour statistics

def getEveningRushHourStats(df):
    
    import pandas as pd
    
    pm25_stats = []
    
    # Select By time

    # set time range for filtering
    start_time = pd.to_datetime('15:00:00', format='%H:%M:%S').time()
    end_time = pd.to_datetime('18:30:00', format='%H:%M:%S').time()

    # filter dataframe by time range
    filtered_df = df[(df['timestamp'].dt.time >= start_time) & (df['timestamp'].dt.time <= end_time)]
    
    pm25_stats = []
    
    if len(filtered_df) == 0:
        
        pm25_stats = [None]*6
    
    else:
    
        # set time range for filtering
        start_time = pd.to_datetime('15:00:00', format='%H:%M:%S').time()
        end_time = pd.to_datetime('18:30:00', format='%H:%M:%S').time()

        # filter dataframe by time range
        filtered_df = df[(df['timestamp'].dt.time >= start_time) & (df['timestamp'].dt.time <= end_time)]

        # find minimum and maximum PM2.5 readings and corresponding timestamps
        min_pm25 = filtered_df['pm25'].min()
        min_pm25_timestamp = filtered_df.loc[filtered_df['pm25'].idxmin(), 'timestamp'].time()
        max_pm25 = filtered_df['pm25'].max()
        max_pm25_timestamp = filtered_df.loc[filtered_df['pm25'].idxmax(), 'timestamp'].time()

        # calculate mean and standard deviation of PM2.5 readings
        mean_pm25 = filtered_df['pm25'].mean()
        std_pm25 = filtered_df['pm25'].std()

        # add results to list
        pm25_stats += [mean_pm25, min_pm25, str(min_pm25_timestamp), max_pm25, str(max_pm25_timestamp), std_pm25]

    return pm25_stats

# Add to storage

summary_stats_names += ['pm25_eveningRush_mean', 'pm25_eveningRush_min', 'pm25_eveningRush_minTime',
                        'pm25_eveningRush_max', 'pm25_eveningRush_maxTime', 'pm25_eveningRush_std'] # Stats Names

summary_stats_dtypes += [float, float, str, float, str, float] # Stat Value Types

summary_stats_functions += [getEveningRushHourStats]

#Daytime ambient statistics

def pm25_daytimeAmbient_stats(df):
    
    import pandas as pd # For some reason this is necessary?
    
    # Select By time
    
    #set the time range for the ambient daytime
    start_daytime_ambient = pd.Timestamp('12:00:00')
    end_daytime_ambient = pd.Timestamp('14:59:59')

    #filter the df by this daytime ambient time range
    filtered_daytime_ambient = df[(df['timestamp'].dt.time >= start_daytime_ambient.time()) & (df['timestamp'].dt.time <= end_daytime_ambient.time())]
    
    stats_list = []
    
    if len(filtered_daytime_ambient) == 0:
        
        stats_list = [None]*6
    
    else:
    

        #get the min, max, std, and average
        pm25_daytimeAmbient_min = filtered_daytime_ambient['pm25'].min()
        mintime = filtered_daytime_ambient.loc[filtered_daytime_ambient['pm25'].idxmin(), 'timestamp'].time()
        pm25_daytimeAmbient_max = filtered_daytime_ambient['pm25'].max()
        maxtime = filtered_daytime_ambient.loc[filtered_daytime_ambient['pm25'].idxmax(), 'timestamp'].time()
        pm25_daytimeAmbient_mean = filtered_daytime_ambient['pm25'].mean()
        pm25_daytimeAmbient_std = filtered_daytime_ambient['pm25'].std()
    
        stats_list =  [pm25_daytimeAmbient_mean, pm25_daytimeAmbient_min, str(mintime), pm25_daytimeAmbient_max, str(maxtime), pm25_daytimeAmbient_std]
    
    return stats_list

# Add to storage

summary_stats_names += ['pm25_daytimeAmbient_mean', 'pm25_daytimeAmbient_min', 'pm25_daytimeAmbient_minTime',
                        'pm25_daytimeAmbient_max','pm25_daytimeAmbient_maxTime', 'pm25_daytimeAmbient_std'] # Stats Names

summary_stats_dtypes += [float, float, str, float, str, float] # Stat Value Types

summary_stats_functions += [pm25_daytimeAmbient_stats]

# ~~~~~

# Stats for Nighttime Ambient

def nighttime_ambient(df):
    
    '''This function considers nighttime to be from midnight to 3AM.
    It gets the min, max, mean, standard deviation for this timeframe
    '''
    
    import pandas as pd # For some reason this is necessary?
    
    # Select by time
    
    starttime = '0:00' # Midnight
    endtime = '3:00' # 3AM
    
    filtered_df = pd.DataFrame(df.values,columns = df.columns, index = df.timestamp)
    
    filtered_df = filtered_df.between_time(starttime, endtime)
    
    stats_list = []
    
    if len(filtered_df) == 0:
        
        stats_list = [None]*6
    
    else:
    
        pms = filtered_df.pm25

        mean = pms.mean()
        min = pms.min()
        mintime = pms[pms == min].index[0].time()
        max = pms.max()
        maxtime = pms[pms == max].index[0].time()
        std = pms.std()
    
        stats_list = [mean, min, str(mintime), max, str(maxtime), std]

    return stats_list
    
# Add to storage

summary_stats_names += ['pm25_nighttimeAmbient_mean', 'pm25_nighttimeAmbient_min', 'pm25_nighttimeAmbient_minTime', 
                        'pm25_nighttimeAmbient_max','pm25_nighttimeAmbient_maxTime', 'pm25_nighttimeAmbient_std'] # Stat Names

summary_stats_dtypes += [float, float, str, float, str, float] # Stat Value Types

summary_stats_functions += [nighttime_ambient]

# ~~~~~