import smtplib
import ssl

def build(body):
	#takes output from parse_post_json, clones the repo from git
	#compiles code - lints python (flake8)
	#return 0 on success, 1 on fail

def test():
	#runs tests

def save_results():
	#creates folder for the commit results - perhaps a separate function called from here
	#creates file with results in folder
		#dependency versions and commit id included
	#updates summary file (in top directory)
    #eg:
              #date, branch, commit-id
              #build: ok
              #test: 7/7
          #or:
              #date, branch, commit-id
              #build: no ok
                  #error message?        #post to api.git (commit status)

def restore():
	#deletes the cloned repo and compiled code in preparation for next webhook
	
	
	
def notify():
	# when code is received
	#	send emails to everyone to tell them code was recieved
	# then tests are done
	# test results are sent to ... everyone? or just the person who sent the code?


def send_email(receiver_email, message):
	"""
	My idea here is that ...
	"""
	sender_email = "continuousintegration2023@gmail.com"
	receiver_email = "continuousintegration2023@gmail.com"
	# password = input(str(“please enter your password : ”))

	message = "Hey, this was sent using python :D" 

	simple_email_context = ssl.create_default_context()

	smtp_port = 587			# Standard secure SMTP port
	smtp_server = "smtp.gmail.com"  # Google SMTP Server

	try:
		server = smtplib.SMTP(smtp_server, smtp_port)
		server.starttls(context=simple_email_context)
		server.login(sender_email, "bengbeng%ED")
		print("Login success")
		print("Sending email to {receiver_email}")
		server.sendmail(sender_email, receiver_email, message) # Sends email
		print("Email has been sent to {receiver_email}")

	except Exception as e:
		print(e)
