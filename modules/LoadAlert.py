import requests
import json

# Constants
baseurl = 'https://cloudhub.io/api/alerts'
headers = {'content-type': 'application/json'}
cloudhub_user = ""
cloudhub_pass = ""

# Cloudhub operations

def load_alert(alert):
	del alert['href']
	del alert['id']
	alert['email']['accountOwner'] = "false"

	response = requests.post(baseurl, headers=headers, data=json.dumps(alert, indent=4), auth=(cloudhub_user, cloudhub_pass))

	if (response.status_code == 201):
		print "Alert successfully loaded in CloudHub,"
	else:
		print "There was an error while uploading alert with HTTP code: " + str(response.status_code)

# Utils
def parseAlert(file_path):
	with open(file_path, "r") as alertFile:
		alert_data = alertFile.read()
		alert_data = alert_data.replace('\n', '')
		alertFile.close()
		return json.loads(alert_data)

# Entry point
def make_request(arguments):
	global cloudhub_user
	global cloudhub_pass

	cloudhub_user = arguments.get('cloudhub_user')
	cloudhub_pass = arguments.get('cloudhub_pass')

	file_path = arguments.get('file_path')
	
	alert = parseAlert(file_path)

	load_alert(alert)