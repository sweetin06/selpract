import pytest


@pytest.mark.smoke

def test_p2():
    msg="hello"
    print(msg)


def test_p3(a,b):
    print(a+b)

test_p3(2,3)

@pytest.fixture()
def setup():
    print("I will be executing first")


def test_fixtureDemo(setup):
    print("I will wxecuted by step os fixture demo")