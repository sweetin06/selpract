import pytest


@pytest.fixture()
def setup():
    driver=driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))