
import unittest
from pages.practice.DoPractice import practice



class Practicetest(unittest.TestCase):

    def setUp(self):
        self.prac=practice()

    def test_run(self):
        mynum=self.prac.factorial(6)
        print(mynum)

    def tearDown(self):
        pass








