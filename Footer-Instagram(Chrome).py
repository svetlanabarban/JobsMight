from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("http://jobmight.com/session/partner/signin")
email = WebDriverWait(driver, 20).until((EC.visibility_of_element_located((By.NAME, "email"))))
email.send_keys("qwe@gmail.com")
password = WebDriverWait(driver, 20).until((EC.visibility_of_element_located((By.NAME, "password"))))
password.send_keys("Qwe-dfg")
login = WebDriverWait(driver, 20).until((EC.element_to_be_clickable((By.XPATH, "//button[contains(@type,'submit')]"))))
login.click()
instagram = WebDriverWait(driver, 20).until((EC.element_to_be_clickable((By.XPATH, "/html/body/div/div/div[2]/div/header/div/div/div/div[5]/div/ul/li[3]/a"))))
instagram.click()