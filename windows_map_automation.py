import time
from appium import webdriver
import unittest
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pynput.keyboard import Key, Controller

keyboard = Controller()
class DesktopAppAutomationTest(unittest.TestCase):
    def setUp(self):
        desired_caps = {
            'platformName': 'Windows',
            'app': 'Microsoft.WindowsMaps_8wekyb3d8bbwe!App'
        }
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        time.sleep(10)

    def test_desktop_app_map_automation(self): # Your test steps go here
        WebDriverWait(self.driver, 90).until(EC.presence_of_element_located((AppiumBy.NAME, "Search")))
        # Enter the location name on search box
        self.driver.find_element(AppiumBy.NAME,"Search").click()
        keyboard.type("BrowserStack Mumbai")
        # Hit the Enter button
        time.sleep(2)
        keyboard.press(Key.enter)
        # Click the direction Button
        self.driver.find_element(AppiumBy.NAME,"Directions").click()
        # click the my Location
        self.driver.find_element(AppiumBy.NAME,", My location, ").click()
        # Click Get direction
        self.driver.find_element(AppiumBy.NAME,"Get directions").click()
        time.sleep(10)

    def tearDown(self):
        self.driver.quit()

if _name_ == '__main__':
    unittest.main()