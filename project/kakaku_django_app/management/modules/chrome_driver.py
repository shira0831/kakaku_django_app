import logging

from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ChromeDriver(object):

    def __init__(self):
        print('init!!')
        self.driver = self.set_driver()


    def set_driver(self):
        options = ChromeOptions()
        options.add_argument(
            "--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36")
        options.add_argument('--ignore-ssl-errors')
        # options.add_argument('--headless')
        capabilities = DesiredCapabilities.CHROME.copy()
        capabilities["acceptInsecureCerts"] = True
        options.add_argument("--window-size=1400,900")
        options.add_argument('--incognito')
        options.add_experimental_option("detach", True)

        return Chrome(executable_path=ChromeDriverManager().install(),
                      options=options,
                      desired_capabilities=capabilities)

    def close_driver(self):
        self.driver.close()
        self.driver.quit()

    def open_url(self, url) :
        self.driver.get(url)

    def window_refresh(self) :
        self.driver.refresh()


    def get_session_id_and_url(self):
        session_url = self.driver.command_executor._url
        session_id = self.driver.session_id
        print(f'driver.command_executor._url: {self.driver.command_executor._url}')
        print(f'driver.session_id: {self.driver.session_id}')

        return [session_id, session_url]


    def wait_displayed_page(self) :
        wait = WebDriverWait(self.driver, 20) 
        wait.until(EC.presence_of_all_elements_located)


    def get_elements(self, target, elements):
        logger = logging.getLogger(__name__)
        elements_ = self.driver.find_elements(By.CSS_SELECTOR, target)

        if not elements_:
            logger.error(
                f"get_elements Failed to get target. target: {target}", exc_info=True)
            return False

        elements.extend(elements_)

        return True


    def get_blocks(self, target):
        
        elements = []
        if self.get_elements(target, elements):
            blocks = elements

        return blocks


    def get_text_css_selector(self, target):
            logger = logging.getLogger(__name__)

            elements = self.driver.find_elements(By.CSS_SELECTOR, target)
            if not elements:
                logger.error(
                    "get_text_css_selector Failed to get target element!", exc_info=True)
                return ''

            return elements[0].text


    def get_text_xpath(self, target):
        logger = logging.getLogger(__name__)

        elements = self.driver.find_elements(By.XPATH, target)
        if not elements:
            logger.error(
                "get_text_xpath Failed to get target element!", exc_info=True)
            return ''

        return elements[0].text


    def get_href_css_selector(self, target):
        logger = logging.getLogger(__name__)

        elements = self.driver.find_elements(By.CSS_SELECTOR, target)
        if not elements:
            logger.error(
                "get_href_css_selector Failed to get target element!", exc_info=True)
            return ''

        return elements


    def get_src(self, target):
            logger = logging.getLogger(__name__)

            elements = self.driver.find_elements(By.XPATH, target)
            if not elements:
                logger.error(
                    "get_src Failed to get target element!", exc_info=True)
                return ''

            return elements[0].get_attribute('src')

    def get_href(self, target):
            logger = logging.getLogger(__name__)

            elements = self.driver.find_elements(By.CSS_SELECTOR, target)
            if not elements:
                logger.error(
                    "get_src Failed to get target element!", exc_info=True)
                return ''

            return elements[0].get_attribute('href')


