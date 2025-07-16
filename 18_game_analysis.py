import pandas as pd

def game_analysis(activity: pd.DataFrame) -> pd.DataFrame:
     first_login_df = activity.groupby('player_id', as_index=False)['event_date'].min()
    
     first_login_df.rename(columns={'event_date': 'first_login'}, inplace=True)
    
     return first_login_df