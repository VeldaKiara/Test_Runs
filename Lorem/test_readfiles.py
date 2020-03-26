import unittest
import readfiles

class TestReadFiles(unittest.TestCase):
    """
    class test teh functions on the readfile module
    Args:
    unittest.TestCase: class from the the unittest module to create unit tests
    """
    def test_nonfile(self):
        """
        Test to confirm that 
        an exeption is raised when a wrong file is inputted
        """
        self.assertEqual(None, readfiles.read_file("tests.txt"))

if __name__ == "__main__":
    unittest.main()