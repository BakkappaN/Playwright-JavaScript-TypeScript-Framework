import pytest
from utils.json.config_reader import ConfigReader
from utils.json.json_testdata_reader import JsonReader

# Logger setup
from utils.logger import get_logger
logger = get_logger(__name__)

def pytest_addoption(parser):
    parser.addoption(
        "--env",
        action="store",
        default="qa",
        help="Environment to run tests"
    )

@pytest.fixture(scope="session")
def app_config(request):
    env = request.config.getoption("--env")
    return ConfigReader.get_config(env)

# read all json test data
@pytest.fixture(scope="session")
def test_data(request):
    env = request.config.getoption("--env")
    return JsonReader.read_all(env)

def pytest_configure(config):
    global pytest_html
    pytest_html = config.pluginmanager.getplugin("html")

# ✅ Correct hook for test start
@pytest.hookimpl(tryfirst=True)
def pytest_runtest_setup(item):
    logger.info(f"Starting test: {item.name}")

# Screenshot on failure
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        page = item.funcargs.get("page")
        if page:
            screenshot_path = f"screenshots/{item.name}.png"
            page.screenshot(path=screenshot_path)

            if hasattr(report, "extra"):
                report.extra.append(pytest_html.extras.image(screenshot_path))
            else:
                report.extra = [pytest_html.extras.image(screenshot_path)]
