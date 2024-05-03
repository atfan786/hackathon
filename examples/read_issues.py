'''
This short example shows how to read the issues from the
provided 'github_issues.pkl' file and how to filter them.
'''

import pandas as pd

# Read issue Dataframe from Pickle file
print('Loading dataframe:')
df = pd.read_pickle('github_issues.pkl')

# Example: Filter issues
print(df.loc[df['state'] != 'open'] )