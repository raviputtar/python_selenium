import pytest
from base.webdriverProvider import webdriverProvider

@pytest.yield_fixture(scope="class")
def getDriverSetup():
    print("getting driver")
    wp=webdriverProvider()
    driver=wp.getwebdriver()


    yield driver
    driver.quit()

@pytest.yield_fixture(scope="class")
def OneTimeSetupPractice():
    baseurl = "https://learn.letskodeit.com/p/practice"
    driver.get(baseurl)

    yield driver
    driver.quit()


@pytest.fixture()
def setUp():
    print("running method level setup")




    yield
    print("running method level teardown")
