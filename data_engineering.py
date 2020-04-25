import pandas as pd

def run_data_engineering(df):
    # use same convention as famsize
    df['age_group'] = 'LE17'
    df['age_group_binary'] = 0
    df.loc[df['age'] > 17, 'age_group'] = 'GT17'
    df.loc[df['age'] > 17, 'age_group_binary'] = 1
    
    df['sex_binary'] = 0
    df.loc[df['sex'] == 'M', 'sex_binary'] = 1
    
    df['famsize_binary'] = 0
    df.loc[df['famsize'] == 'LE3', 'famsize_binary'] = 1
    
    df['health_group'] = 'bad'
    df['health_group_binary'] = 0
    df.loc[df['health'] >= 4, 'health_group'] = 'good'
    df.loc[df['health'] >= 4, 'health_group_binary'] = 1
    
    df['grade_group'] = 'low'
    df['grade_group_binary'] = 0
    df.loc[df['G3'] > 13, 'grade_group'] = 'high'
    df.loc[df['G3'] > 13, 'grade_group_binary'] = 1
    
    return df