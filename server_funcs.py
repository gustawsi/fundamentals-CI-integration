import requests
import unittest
import subprocess


def build(body):
	#takes output from parse_post_json, clones the repo from git
	#compiles code - lints python (flake8)
	#return 0 on success, 1 on fail


def test(temp_path):
    """
    function runs the test.py file from the server
    and returns array with number of tests passed and total number of tests
    """
    test_path = temp_path + '/test/test.py'
    
    test_suite = unittest.TestLoader().loadTestsFromTestCase(test_path)
    tests_run = unittest.TextTestRunner(verbosity=2).run(test_suite)
    tests_passed = tests_run.testsRun - len(tests_run.failures)

    return (tests_passed, tests_run.testsRun)


    print('Result:', tests_passed.wasSuccessful())
    for failure in tests_passed.failures:
        print('Failure:', failure[0])

    results = test.test_file_exists()
    print("Passed:", results[0], "of", results[1], "tests.")

  

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