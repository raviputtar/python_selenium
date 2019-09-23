import pytest
import unittest
from pages.practice.DoPractice import practice



class Practicetest(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self):
        self.prac=practice()

    def test_run(self,OneTimeSetupPractice):
        self.prac.click_dropdown("Honda")




