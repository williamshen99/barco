import sys
import platform
import logging
from selenium import webdriver
from configparser import ConfigParser


class Setup:
    def __init__(self, args):
        self.setup_config = ConfigParser()
        self.setup_config.read('config/setup.cfg')
        self.project_config = ConfigParser()
        self.project_config.read('config/project.cfg')
        self.browser = BrowserWebDriver(self.setup_config, args['browser'])
        self.driver = self.browser.get_webdriver()
        self.env = TestEnv(self.project_config, args['test_env'])


class BrowserWebDriver:
    def __init__(self, setup_config, browser):
        self.setup_config = setup_config
        self.set_browser(browser)
        self.driver = self.initialize_webdriver(self.browser)

    def set_browser(self, browser):
        if browser is not None:
            self.browser = browser.upper()
            logging.info('browser is set from args: %s', self.browser)
        else:
            self.browser = self.setup_config.get('WebDriver', 'BROWSER').upper()
            logging.info('browser is set from setup.cfg: %s', self.browser)

    def initialize_webdriver(self, browser):
        driver = self.get_local_webdriver(browser)
        driver.set_window_size(1600, 1200)
        logging.info('set windows size: %s', driver.get_window_size())
        return driver

    def get_local_webdriver(self, browser):
        webdriver = {
            'CHROME': self.get_chrome_webdriver
        }
        logging.info('local webdriver: %s', webdriver[browser])
        return webdriver[browser]()

    def get_chrome_webdriver(self):
        path = driver = None

        options = webdriver.chrome.options.Options()
        options.add_argument("incognito")

        # win webdriver
        if sys.platform == 'win32':
            path = self.setup_config.get('WebDriver', 'CHROME_WIN_PATH')
            driver = webdriver.Chrome(path)

        # mac webdriver
        elif sys.platform == 'darwin':
            path = self.setup_config.get('WebDriver', 'CHROME_MAC_PATH')
            driver = webdriver.Chrome(path, options=options)

        # linux webdriver
        elif 'linux' in sys.platform:
            if platform.architecture()[0] == '64bit':
                path = self.setup_config.get('WebDriver', 'CHROME_LINUX_PATH')
            else:
                raise ValueError('x64 only')
            driver = webdriver.Chrome(path)

        return driver

    def get_webdriver(self):
        return self.driver

    def teardown_webdriver(self):
        self.driver.close()
        self.driver.quit()


class TestEnv:

    def __init__(self, project_config, env):
        self.project_config = project_config
        self.set_env(env)
        self.click_share_support_warranty_info_host = project_config.get(self.env, 
                                                                         'CLICK_SHARE_SUPPORT_WARRANTY_INFO_HOST')

    def set_env(self, env):
        if env is not None:
            self.env = env.upper()
            logging.info('testing env is set from args: %s', self.env)
        else:
            self.env = self.project_config.get('TestEnv', 'TEST_ENV').upper()
            logging.info('testing env is set from setup.cfg: %s', self.env)
