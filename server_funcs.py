import git
import os
import config 
import tempfile


def build(body):
	#takes output from parse_post_json, clones the repo from git
	#compiles code - lints python (flake8)
	#return 1 on success, 0 on fail

	temp_dir = tempfile.TemporaryDirectory()
	temp_path = config.temp_repo_path + temp_dir.name
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