from selenium import webdriver
# from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.minimize_window()

driver.get ('https://www.tiket.com/')
print(driver.title)
driver.get ('https://www.tokopedia.com/')
print(driver.title)
driver.get ('https://www.orangsiber.com/')
print(driver.title)
driver.get ('https://demoqa.com/')
print(driver.title)
driver.get ('https://automatetheboringstuff.com/')
print(driver.title)
driver.close()

