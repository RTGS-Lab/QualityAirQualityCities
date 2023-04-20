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

## Min/Max

def getminmax(df):
    max = df.pm25.max()
    min = df.pm25.min()
    
    return [min, max]

# Add to storage

summary_stats_names += ['min', 'max'] # Stat Names

summary_stats_dtypes += [float, float] # Stat Value Types

summary_stats_functions += [getminmax]

# ~~~~~

# Morning rush hour statistics

df['timestamp'] = pd.to_datetime(df.timestamp)

def pm25_morningRush_stats(df):
    df_6_to_9 = df.loc[(df['timestamp'].dt.hour >= 6) & (df['timestamp'].dt.hour < 9)]
    
    pm25_morningRush_min = df_6_to_9['pm25'].min()
    pm25_morningRush_max = df_6_to_9['pm25'].max()
    pm25_morningRush_mean = df_6_to_9['pm25'].mean()
    pm25_morningRush_std = df_6_to_9['pm25'].std()
    
    return [pm25_morningRush_min, pm25_morningRush_max, pm25_morningRush_mean, pm25_morningRush_std]

# Add to storage

summary_stats_names += ['pm25_morningRush_min', 'pm25_morningRush_max', 'pm25_morningRush_mean', 'pm25_morningRush_std'] # Stat Names

summary_stats_dtypes += [float, float, float, float] # Stat Value Types

summary_stats_functions += [pm25_morningRush_stats]

# ~~~~~
#Daytime ambient statistics

def pm25_daytimeAmbient_stats(df):
    df['timestamp'] = pd.to_datetime(df.timestamp)
    
    #set the time range for the ambient daytime
    start_daytime_ambient = pd.Timestamp('12:00:00')
    end_daytime_ambient = pd.Timestamp('14:59:59')

    #filter the df by this daytime ambient time range
    filtered_daytime_ambient = df[(df['timestamp'].dt.time >= start_daytime_ambient.time()) & (df['timestamp'].dt.time <= end_daytime_ambient.time())]

    #get the min, max, std, and average
    pm25_daytimeAmbient_min = filtered_daytime_ambient['pm25'].min()
    pm25_daytimeAmbient_max = filtered_daytime_ambient['pm25'].max()
    pm25_daytimeAmbient_mean = filtered_daytime_ambient['pm25'].mean()
    pm25_daytimeAmbient_std = filtered_daytime_ambient['pm25'].std()
    
    return [pm25_daytimeAmbient_min, pm25_daytimeAmbient_max, mean_dytm_amb, std_dev_dytm_amb]
# Add to storage

summary_stats_names += ['pm25_daytimeAmbient_min', 'pm25_daytimeAmbient_max', 'pm25_daytimeAmbient_mean','pm25_daytimeAmbient_std'] # Stat Names

summary_stats_dtypes += [float, float, float, float] # Stat Value Types

summary_stats_functions += [pm25_daytimeAmbient_stats]
# ~~~~~