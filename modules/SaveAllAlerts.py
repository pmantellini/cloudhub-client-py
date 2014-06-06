import requests
import json

# Constants
baseurl = 'https://cloudhub.io/api/alerts'
cloudhub_user = ""
cloudhub_pass = ""

# Cloudhub operations

def get_alerts():
	query_string  =  {
	      "limit": 50,
	      "offset": 0
	}

	page_counter = 0
	has_next = True

	# Automatic Pagination
	while (has_next):
		query_string["offset"] = (page_counter * query_string["limit"])
		response = requests.get(baseurl, params=query_string, auth=(cloudhub_user, cloudhub_pass))

		if (response.status_code == 200):
			json_response = json.loads(response.text)
			alert_list = json_response['data']
		
			for alert in alert_list:
				alertSaver(alert, 'alert_' + cloudhub_user.replace('@','_') + '_' +  alert['name'] + '.json')

		page_counter += 1 
		if (json_response["total"] < (page_counter * query_string["limit"])):
			has_next = False

		pass

# Utils
def alertSaver(alert, file_path):
	with open(file_path, "w") as outputFile:
		json.dump(alert, outputFile, indent=4)
		outputFile.close()

# Entry point
def make_request(arguments):
	global cloudhub_user
	global cloudhub_pass

	cloudhub_user = arguments.get('cloudhub_user')
	cloudhub_pass = arguments.get('cloudhub_pass')

	get_alerts()