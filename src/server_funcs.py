import smtplib
import ssl
import git
import os
import tempfile
import json
import config
from datetime import datetime

def create_temp_path():
    """
    Creates a path to a temporary directory where the repo can be stored
    """
    temp_dir = tempfile.TemporaryDirectory()
    return config.temp_repo_path + temp_dir.name


def parse_post_data(post_byte_data):
    """
    Takes in the bytedata from the post requests and converts it into a json.
    Important information is then extracted to create a new json file called body_data.
    """
    # Decode UTF-8 bytes to Unicode, and convert single quotes to double quotes to make it valid JSON
    post_json = post_byte_data.decode('utf8').replace("'", '"')
    request = json.loads(post_json)

    # parses the post body into a format handled by the build function
    url = request["repository"]["html_url"]
    ref = request["ref"]
    branch = ref.replace("/", " ").split(" ")[-1]
    pusher_email = request["pusher"]["email"]

    body_data = {
        "url": url,
        "ref": ref,
        "branch": branch,
        "pusher_email": pusher_email,
    }
    return body_data


def build(body, temp_path):
    """
    Takes output from parse_post_json, clones the repo from git
    compiles code - lints python (flake8)
    return 1 on success, 0 on fail
    """
    git.Repo.clone_from(body["url"], os.path.join(
        temp_path), branch=body["branch"])
    res = os.system("python3 " + temp_path + " flake8")
    if res == 0:
        return 1
    else:
        return 0


def test():
    """
    TBD
    """
    print()
    # runs tests


def save_results(body_data, build_res, test_res, temp_path):
    """
    :param body data: JSON format HTTP Post data
    :param build_res: Integer: either 1 or 0
    :param test_res: String, either has value True or contains information as to what tests passed
    :param temp_path: Temp path to git repo directory

    :return: String containing:

    Function gets commit information from cloned repo, adds test information and outputs
    result in a readable format by sending an email.
    """

    repo = temp_path
    tree = repo.tree()
    id = tree.commit_id
    commit = next(repo.iter_commits(paths=tree[0].path, max_count=1))
    date = commit.committed_date
    date_datetime = datetime.utcfromtimestamp(
        date).strftime('%Y-%m-%d %H:%M:%S')

    commit_id = id
    commit_date = date_datetime
    commit_branch = body_data["branch"]
    committed_by = body_data["pusher_email"]

    # Set result contents
    build_status = ""
    if build_res == 1:
        build_status = "ok"
    elif build_res == 0:
        build_status = "not ok"
    test_status = ""
    if test_res == True:  # True or anything signaling all tests have been passed.
        test_status = "all tests passed!"
    else:
        test_status = test_res  # Passes / total amount of tests
    ##

    # Construct Out string with build information
    out = ""
    out += "commit-date: " + str(commit_date) + "\n" + "pushed_by: " + str(committed_by) + "\n" + "branch: " + \
        str(commit_branch) + "\n" + "commit-id: " + str(commit_id) + "\n" + "build-status: " + (build_status) + "\n" +\
        "tests-status: " + str(test_status)

    return out





def restore():
    """
    TBD
    """
    print()
    # deletes the cloned repo and compiled code in preparation for next webhook


def notify():
    """
    TBD
    """
    print()
    # when code is received
    #	send emails to everyone to tell them code was recieved
    # then tests are done
    # test results are sent to ... everyone? or just the person who sent the code?


def send_email(receiver_email, message):
    """
    Sends an email with the test results
    """
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
        server.sendmail(sender_email, receiver_email, message)  # Sends email
        print("Email has been sent to", receiver_email)

    except Exception as e:
        print(e)
