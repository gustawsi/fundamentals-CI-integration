import unittest, sys
sys.path.append("..")

from subprocess import run
import src.config

class TestServer(unittest.TestCase):
    repopath = src.config.temp_repo_path

    def test_dir_size_not_zero(self):
        size = run(['bash', 'size.sh', self.repopath],capture_output=True,text=True)
        self.assertTrue(int(size.stdout) > 0)
    
    def test_file_exists(self):
        size = run(['bash', 'num_files.sh', self.repopath],capture_output=True,text=True)
        self.assertTrue(int(size.stdout) > 0)


if __name__ == '__main__' :
    unittest.main()
