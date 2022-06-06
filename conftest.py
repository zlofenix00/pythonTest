import pytest as pytest

from utils.driver import Driver
from utils.driver import DriverCreator


@pytest.fixture(autouse=True)
def webdriver(request):
    Driver()._test_name = request.node.name
    yield
    Driver().quit()
    DriverCreator.destroy_instance()
