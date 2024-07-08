import time
import security3
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

URLLogin = 'https://dev.everex.ai/signin'
account3 = security3.account2()

options = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=options)
driver.get(url=URLLogin)

wait = WebDriverWait(driver, 10)  # 최대 10초 대

#쿠키창 노출 > 쿠키 허가 (쿠키는 3번 쿠키만 허가함)
cookieconsent = driver.find_element(By.XPATH, '//*[@id="app"]/div[3]/div')
managecookieBtn = driver.find_element(By.XPATH, '//*[@id="app"]/div[3]/div/div/div/button')

if managecookieBtn:
 print("managecookieBtn")

managecookieBtn.click()

cookieacptBtn = cookieconsent.find_element(By.XPATH, '//*[@id="app"]/div[3]/div/div/div/div/button[2]')
if cookieacptBtn:
 print("cookieacptBtn")

cookierejtBtn = cookieconsent.find_element(By.XPATH, '//*[@id="app"]/div[3]/div/div/div/div/button[1]')
if cookierejtBtn:
 print("cookierejtBtn")

time.sleep(1)

 
# 쿠키 설정 변경 (쿠키는 3번 쿠키만 허가함)
PerformanceCookiesBtn = cookieconsent.find_element(By.XPATH, '//*[@id="app"]/div[3]/div/div/div[2]/div[3]/div[2]/label/span')
PerformanceCookiesBtn.click()
time.sleep(1)

SaveMyPreferencesBtn = cookieconsent.find_element(By.XPATH, "//*[text()='Save My Preferences']")
SaveMyPreferencesBtn.click()
time.sleep(1)


# 로그인
emailinput = driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div')
emailinput.click()
input = driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div/input').send_keys(account3.get("email"))
time.sleep(3)
input = driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[3]/div/input').send_keys(account3.get("password"))
time.sleep(3)
loginBtn = driver.find_element('xpath', '//*[@id="app"]/div[1]/div[2]/div[2]/div/button')
loginBtn.click()

print("3번 쿠키 허가 후 로그인 성공")

time.sleep(10)




