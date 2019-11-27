# Generated by Selenium IDE
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


class GatewayReboot():
    def setup_method(self, gateway_password, standalone_chrome):
        # prepare the option for the chrome driver
        # options = webdriver.ChromeOptions()
        # options.add_argument('headless')
        # self.driver = webdriver.Chrome(options=options)
        self.driver = webdriver.Remote(
            command_executor=standalone_chrome,
            desired_capabilities=DesiredCapabilities.CHROME)
        self.gateway_password = gateway_password

    def teardown_method(self):
        self.driver.quit()

    def reboot(self):
        # Test name: reboot
        # Step # | name | target | value | comment
        # 1 | open | /cgi-bin/luci |  |
        self.driver.get("http://192.168.1.1/cgi-bin/luci")
        # 2 | setWindowSize | 1485x1068 |  |
        self.driver.set_window_size(1485, 1068)
        # 3 | click | id=login_password |  |
        self.driver.find_element(By.ID, "login_password").click()
        # 4 | type | id=login_password | 123 |
        self.driver.find_element(By.ID, "login_password").send_keys(self.gateway_password)
        # 5 | click | css=.btn |  |
        self.driver.find_element(By.CSS_SELECTOR, ".btn").click()
        # 6 | click | id=menu_action_restart_hint |  |
        self.driver.find_element(By.ID, "menu_action_restart_hint").click()
        # 7 | click | id=confirm |  |
        self.driver.find_element(By.ID, "confirm").click()
