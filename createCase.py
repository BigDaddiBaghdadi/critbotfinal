from jira import JIRA
import schedule
import time

options = {'server': 'https://slingpower.atlassian.net/'}
jira = JIRA(options, basic_auth=('slingpower@gmail.com', 'vaQvu1ccFcFfnEl6aty6839D'))

def create_new_issue():
    new_issue = jira.create_issue(project='AO', summary='Test issue',
                                  description='This is a test issue', issuetype={'name': 'Bug'})
    print(f'New issue created with key: {new_issue.key}')

schedule.every(5).seconds.do(create_new_issue)

while True:
    schedule.run_pending()
    time.sleep(1)
