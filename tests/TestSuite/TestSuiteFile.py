import unittest

from tests.courses.register_course_tests import RegisterCourseTests
from tests.home.login_test import logintest
#from tests.practice.practiceTest import practice


tc1=unittest.TestLoader().loadTestsFromTestCase(logintest)
tc2=unittest.TestLoader().loadTestsFromTestCase(RegisterCourseTests)
#tc3=unittest.TestLoader.loadTestsFromTestCase(practiceTe)

my_suite=unittest.TestSuite([tc1,tc2])

unittest.TextTestRunner(verbosity=2).run(my_suite)

