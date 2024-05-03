'''
This example shows how we fetched the issues from the Infineon organisation on GitHub.
Feel free to modify this code and fetch the issues again depending on your preferences.
If you run into API limits you can talk to us, maybe we can fetch some data for you using our access tokens.
'''

from github import Github
from datetime import datetime, timedelta
import pandas as pd

def main():
    
    try:
        import secret
        github = Github(secret.access_token)
    except:
        github = Github()
    
    github_org = 'Infineon'
    ifx = github.get_organization(github_org)

    # Go through all open GitHub issues and put them in a Pandas Dataframe
    
    df = pd.DataFrame()

    for repo in ifx.get_repos():
        print(f'Working on repo {repo.name}...')
        issues = repo.get_issues(state='all') # state='all' -> we also take closed issues for training.
        for issue in issues:
            if issue.pull_request == None: issue_type = 'issue'
            else: issue_type = 'pull-request'
            issue_data = {
                'id': [issue.id],
                'title': [issue.title],
                'repo_name': [repo.name],
                'pr': [issue_type],
                'state': [issue.state],
                'created': [issue.created_at],
                'updated': [issue.updated_at],
                'body': [issue.body],
                'user_login': [issue.user.login],
                'url': [issue.url],
                'comments': [issue.comments],
                'user_type': [issue.user.type],
                'labels': [issue.labels],
                'assignees': [issue.assignees]
            }
            df = pd.concat([
                df, 
                pd.DataFrame(issue_data)
                ], ignore_index=True)
        # For testing: End loop after first few issues
        # if not df.empty: break

    # Make the issue ID the Dataframe index
    df.set_index('id', inplace=True)

    # Write Dataframe to Pickle file
    print('Saving dataframe:')
    print(df)
    df.to_pickle('github_issues.pkl')

    # Test readback from Pickle file
    print('Loading dataframe:')
    df = pd.read_pickle('github_issues.pkl')
    print(df)

if __name__ == '__main__':
    main()