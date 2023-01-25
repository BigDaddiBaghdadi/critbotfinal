from jira import JIRA
import schedule 


# Set up connection to JIRA
options = {'server': 'https://slingpower.atlassian.net'}
jira = JIRA(options, basic_auth=('slingpower@gmail.com', 'awqcg757MrtbZuragBiM52DB'))

# Search for unassigned issues
unassigned_issues = jira.search_issues("assignee = empty")

# Assign issues to yourself
for issue in unassigned_issues:
    jira.assign_issue(issue, 'slingpower@gmail.com')

print(f'{len(unassigned_issues)} issues assigned to your_username')
