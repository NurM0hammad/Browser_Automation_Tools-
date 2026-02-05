from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

class BrowserController:
    def __init__(self, browser_type='chrome'):
        if browser_type == 'chrome':
            self.driver = webdriver.Chrome()
        elif browser_type == 'firefox':
            self.driver = webdriver.Firefox()
        else:
            raise ValueError("Unsupported browser type")
    
    def open_url(self, url):
        self.driver.get(url)
        self.driver.maximize_window()
    
    def click_element(self, locator_type, locator):
        element = self.driver.find_element(getattr(By, locator_type.upper()), locator)
        element.click()
    
    def type_text(self, locator_type, locator, text):
        element = self.driver.find_element(getattr(By, locator_type.upper()), locator)
        element.clear()
        element.send_keys(text)
    
    def get_text(self, locator_type, locator):
        element = self.driver.find_element(getattr(By, locator_type.upper()), locator)
        return element.text
    
    def take_screenshot(self, filename="screenshot.png"):
        self.driver.save_screenshot(filename)
    
    def close(self):
        self.driver.quit()

# Usage example
bot = BrowserController()
try:
    bot.open_url("https://www.google.com")
    bot.type_text("NAME", "q", "Python automation tutorial")
    bot.click_element("NAME", "btnK")
    time.sleep(2)
    bot.take_screenshot("google_search.png")
finally:
    bot.close()