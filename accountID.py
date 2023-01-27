import requests

# Make a GET request to the myself endpoint
response = requests.get('https://slingpower.atlassian.net/rest/api/2/myself', auth=('slingpower@gmail.com', 'vaQvu1ccFcFfnEl6aty6839D'))

# Get the account ID from the JSON response
data = response.json()
account_id = data['accountId']
print("Account ID:", account_id)
