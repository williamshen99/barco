import logging
import pytest
from config.setup import Setup
from pages import click_share_support


def pytest_addoption(parser):
    parser.addoption('--browser', help='browser to test: Chrome / Firefox / IE', default='Chrome')
    parser.addoption('--test_env', help='test environment: Stage / Test / Production', default='test')


@pytest.yield_fixture()
def setup(request):
    args = {
        'browser': request.config.getoption('--browser'),
        'test_env': request.config.getoption('--test_env'),
    }
    logging.info('input args: %s', args)
    setup = Setup(args)
    if request.cls is not None:
        request.cls.setup = setup
    setup.click_share_support = click_share_support.ClickShareSupportPage(setup.driver)

    yield setup
    setup.browser.teardown_webdriver()


@pytest.yield_fixture()
def go_to_click_share_support_page(setup):
    url = setup.env.click_share_support_warranty_info_host

    setup.click_share_support.open_page(url)
    
    return setup
