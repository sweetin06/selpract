import pytest


@pytest.fixture()
def setup():
    print("I will be executing first")
    yield #hold
    print("executed last")



def test_fixtureDemo(setup):
    print("I will wxecuted by step os fixture demo")