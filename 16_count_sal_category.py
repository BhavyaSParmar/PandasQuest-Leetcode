import pandas as pd

def count_salary_categories(accounts: pd.DataFrame) -> pd.DataFrame:
    def categorize(income):
        if income < 20000:
            return 'Low Salary'
        elif income <= 50000:
            return 'Average Salary'
        else:
            return 'High Salary'
    accounts['category'] = accounts['income'].apply(categorize)
    
    counts = accounts.groupby('category').size().reset_index(name='accounts_count')
    
    all_categories = pd.DataFrame({
        'category': ['Low Salary', 'Average Salary', 'High Salary']
     })
    
    result = all_categories.merge(counts, on='category', how='left').fillna(0)
    result['accounts_count'] = result['accounts_count'].astype(int)
    
    return result
