from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Setup
driver = webdriver.Chrome()  # or Firefox(), Edge(), etc.
driver.get("nimble-kitten-2445a2.netlify.app")

# Find elements and interact
search_box = driver.find_element(By.NAME, "q")
search_box.send_keys("Python automation")
search_box.send_keys(Keys.RETURN)

# Wait for elements
wait = WebDriverWait(driver, 10)
element = wait.until(EC.presence_of_element_located((By.ID, "result")))

# Close browser
driver.quit()