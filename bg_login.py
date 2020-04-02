import time
from selenium.webdriver import Chrome

chromeDriver = 'C:\\temp\\chromedriver.exe'

driver = Chrome(chromeDriver)

driver.get('https://accounts.kakao.com/login?continue=https%3A%2F%2Flogins.daum.net%2Faccounts%2Fksso.do%3Frescue%3Dtrue%26url%3Dhttp%253A%252F%252Fpubg.game.daum.net%252Fpubg%252Findex.daum')

time.sleep(3)

input_login = driver.find_element_by_id("id_email_2")
input_login.send_keys("rlatmd017@naver.com")

input_password = driver.find_element_by_id("id_password_3")
input_password.send_keys("gkskvhqnvhtn123")

btn = driver.find_element_by_class_name("btn_g")

time.sleep(1)

btn.click()

time.sleep(3)

game_start = driver.find_element_by_id("a_gnb_game_start")
game_start.click()

time.sleep(5)

driver.quit()
