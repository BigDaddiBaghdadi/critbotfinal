from jira import JIRA
import jira.client

# Set up connection to JIRA
options = {'server': 'https://slingpower.atlassian.net'}
# Connect to JIRA
jira = jira.client.JIRA(options=options, basic_auth=('slingpower@gmail.com', 'vaQvu1ccFcFfnEl6aty6839D'))

# Specify the project key
project_key = 'AO'

# Get all issues in the specified project
issues = jira.search_issues('project = {}'.format(project_key))

# Print the names of all issues
for issue in issues:
    print(issue.fields.summary)

# Assign all unassigned issues to slingpower@gmail.com
assignee = "616346cdc669a60069b75d56"

# use jira.fields to get the list of fields
fields = jira.fields()
for field in fields:
    print(field['name'])
    
unassigned_issues = jira.search_issues("assignee is empty and project = " + project_key)
for issue in unassigned_issues:
    jira.transition_issue(issue,'31')
    jira.assign_issue(issue, assignee)
