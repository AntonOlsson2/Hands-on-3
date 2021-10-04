import md
import os
import sys, unittest

md.run_md()
class MdTests(unittest.TestCase):
    def test_calcenergy(self):
        path = '/home/antol302/project-hands-on/hands-on-3/cu.traj'
        if os.path.isfile(path):
            self.assertTrue(True)

if __name__ == "__main__":
    tests = [unittest.TestLoader().loadTestsFromTestCase(MdTests)]
    testsuite = unittest.TestSuite(tests)
    result = unittest.TextTestRunner(verbosity=0).run(testsuite)
    sys.exit(not result.wasSuccessful())
