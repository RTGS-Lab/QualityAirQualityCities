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