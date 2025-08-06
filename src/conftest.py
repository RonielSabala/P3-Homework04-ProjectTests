import pytest
from pathlib import Path
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption(
        "--base-url",
        action="store",
        default="http://localhost:1111",
        help="Base URL de la aplicación",
    )


@pytest.fixture(scope="session")
def base_url(request):
    return request.config.getoption("base_url")


@pytest.fixture(scope="function")
def driver(request):
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    yield driver
    driver.quit()


@pytest.fixture(scope="function")
def capture_dir(request):
    test_name = request.node.name
    story = Path(request.node.fspath).parent.name
    base = Path(request.config.rootdir) / "results/captures" / story / test_name
    base.mkdir(parents=True, exist_ok=True)
    return str(base)
