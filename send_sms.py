from flask import Flask, request
from twilio.rest import Client


def send_response (body = "NULL", rcv_from = "+10000000000", country="Default_country"):
	client = Client(account_sid, auth_token)
	message = client.messages.create(to=str(rcv_from), from_=from_number,
	              body="Hi! It looks like your phone number was born in {{ " + country + "  }}")
	return ("OK")

app = Flask(__name__)
@app.route('/sms', methods=['GET', 'POST'])
def handler():
	if request.method == "POST":
		send_response("DUMMY_BODY", request.form['From'], request.form['FromCountry'])
		print("\n\n****Rcv POST****\n\n")
		return 'OK'
	else:
		print(request.headers)
		print("\n\n****Rcv GET****\n\n")
		return 'OK'


if __name__=='__main__':

	#Get the details about your account from the console page
	#of Twilio https://www.twilio.com/console

	print ("Go to https://www.twilio.com/console and sign-in to get the below details")
	account_sid = input("Enter your Twilio account_sid:")
	auth_token = input("Enter your Twilio auth_token:")
	from_number = input("Enter your Twilio phone number:")
	client = Client(account_sid, auth_token)

	#Set the debug mode to True to catch
	# exceptions in Flask easily
	# PS, the flask app creation re-runs when it is set to True
	app.run(debug = False, port=8888)

	#1. Use ngrok to create a global UR
	#2. Ensure that ngrok runs on the same port
	#   as the python flask server './ngrok http 8889'



