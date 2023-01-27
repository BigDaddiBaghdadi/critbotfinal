from jira import JIRA
import schedule
import time

options = {'server': 'https://slingpower.atlassian.net/'}
jira = JIRA(options, basic_auth=('slingpower@gmail.com', 'NbL8pGhAlfptBVFlirSBC0EF'))

def close_issues():
    assigned_issues = jira.search_issues("assignee = 'slingpower@gmail.com'")
    for issue in assigned_issues:
        
        # Get the transition id for the "Close" transition
        transitions = jira.transitions(issue)
        close_transition = [t for t in transitions if t['name'] == 'In Progress'][0]
        close_transition_id = close_transition['id']

        # Perform the transition
        jira.transition_issue(issue, close_transition_id)
    print(f'{len(assigned_issues)} issues in Progress')


#schedule.every(5).seconds.do(close_issues)

#while True:
    #schedule.run_pending()
    #time.sleep(1)
