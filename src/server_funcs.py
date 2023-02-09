import smtplib
import ssl
import git
import os
import config
import tempfile


def create_temp_path():
	temp_dir = tempfile.TemporaryDirectory()
	return config.temp_repo_path + temp_dir.name

def build(body, temp_path):
	#takes output from parse_post_json, clones the repo from git
	#compiles code - lints python (flake8)
	#return 1 on success, 0 on fail
	git.Repo.clone_from(body["url"], os.path.join(temp_path), branch=body["branch"])
	res = os.system("python3 " + temp_path + " flake8")
	if res == 0:
		return 1
	else: 
		return 0

def test():
	print()
	#runs tests

def save_results():
	print()
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
	print()
	#deletes the cloned repo and compiled code in preparation for next webhook
	
	
	
def notify():
	print()
	# when code is received
	#	send emails to everyone to tell them code was recieved
	# then tests are done
	# test results are sent to ... everyone? or just the person who sent the code?



def send_email(receiver_email, message):
	sender_email = "continuousintegration2023@gmail.com"
	# the password will be integrated into the code but not here on github :)
	password = input(str("please enter your password : ")) 
	simple_email_context = ssl.create_default_context()
	smtp_port = 587			# Standard secure SMTP port
	smtp_server = "smtp.gmail.com"  # Google SMTP Server

	try:
		server = smtplib.SMTP(smtp_server, smtp_port)
		server.starttls(context=simple_email_context)
		server.login(sender_email, password)
		server.sendmail(sender_email, receiver_email, message) # Sends email
		print("Email has been sent to", receiver_email)

	except Exception as e:
		print(e)
