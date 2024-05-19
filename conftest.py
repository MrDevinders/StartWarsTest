from datetime import datetime
from pathlib import Path
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import pytest

BaseUrl = "http://localhost:3000/"
ImplicitWait = 30


@pytest.fixture(scope="class", autouse=True)
def browser_setup(request):
    global driver

    options = Options()
    options.add_experimental_option("detach", True)

    options.add_argument("--start-maximized")
    options.add_argument("--disable-extensions")
    options.add_argument("--disable-gpu ")
    options.add_argument("--no-sandbox")
    options.add_argument("--user-agent=Automated Test")
    options.add_argument("--ignore-certificate-errors")
    options.add_argument("--disable-extensions")
    options.add_argument("--disable-web-security")
    options.add_argument("--disable-web-security")
    options.add_argument("--disable-popup-blocking")
    options.add_argument("--disable-default-apps")
    options.add_argument("test-type=browser")
    #options.add_argument("--headless")

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),
                        options=options)

    request.cls.driver = driver

@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    global report_dir

    today = datetime.now()
    report_dir = Path("reports", today.strftime("%Y%m%d"))
    report_dir.mkdir(parents=True, exist_ok=True)
    pytest_html = report_dir / f"Report_{today.strftime('%Y%m%d%H%M')}.html"
    config.option.htmlpath = pytest_html
    config.option.self_contained_html = True


def pytest_html_report_title(report):
    report.title = "star-wars Automation Test Report"


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call' or report.when == 'setup':
        xfail = hasattr(report, 'wasxfail')
#        if (report.skipped and xfail) or (report.failed and not xfail):
        file_name = report.nodeid.replace("::", "_") + ".png"

        scr_dir = Path(report_dir, "screens")
        scr_dir.mkdir(parents=True, exist_ok=True)
        scr_file = "screens/" + file_name.split('/')[1]
        file_name = scr_dir / f"{file_name.split('/')[1]}"

        _capture_screenshot(file_name)
        if file_name:
            html = '<div><img src="%s" alt="screenshot" style=width:304px;height:228px; onclick="window.open(this.src)" align="right"/></div>' % scr_file
            extra.append(pytest_html.extras.html(html))

        report.extra = extra

def _capture_screenshot(name):
    driver.get_screenshot_as_file(name)
