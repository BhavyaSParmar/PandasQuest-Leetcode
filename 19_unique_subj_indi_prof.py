import pandas as pd

def count_unique_subjects(teacher: pd.DataFrame) -> pd.DataFrame:
     unique_subjects = teacher.drop_duplicates(subset=['teacher_id', 'subject_id'])
   
     result = unique_subjects.groupby('teacher_id').agg(cnt=('subject_id', 'count')).reset_index()
    
     return result