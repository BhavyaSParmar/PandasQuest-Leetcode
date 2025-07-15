import pandas as pd

def total_time(employees: pd.DataFrame) -> pd.DataFrame:
     employees['duration'] = employees['out_time'] - employees['in_time']

     result = ( employees.groupby(['event_day', 'emp_id'])['duration']
        .sum()
        .reset_index()
        .rename(columns={'event_day': 'day', 'duration': 'total_time'})
    )
    
     return result