import pytest
from base.webdriverProvider import webdriverProvider

@pytest.yield_fixture(scope="class")
def OneTimeSetup():
    print("getting driver")
    wp=webdriverProvider()
    driver=wp.getwebdriver()
    baseurl = "https://letskodeit.teachable.com/"
    driver.get(baseurl)

    yield driver



@pytest.fixture()
def setUp():
    print("running method level setup")




    yield
    print("running method level teardown")
