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