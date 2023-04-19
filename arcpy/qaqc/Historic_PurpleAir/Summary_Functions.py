### This script will store all of our Daily Summary Functions

### Storage

summary_stats = [] # Stat Names

summary_stats_dtypes = [] # Stat Value Types

summary_stats_functions = [] # The functions

### Functions
# These should return the stats as a list (even if it is just one stat)

def n_observations(df):
    
    return [len(df)]

# Add to storage

summary_stats += ['n_observations'] # Stat Names

summary_stats_dtypes += [int] # Stat Value Types

summary_stats_functions += [n_observations]