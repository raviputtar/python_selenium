import pytest
import unittest
from pages.practice.DoPractice import practice



class Practicetest(unittest.TestCase):

    def classSetup(self):
        self.prac=practice()

    def test_run(self,OneTimeSetupPractice):
        self.prac.click_dropdown("Honda")



if __name__ == '__main__':
    unittest.main()
