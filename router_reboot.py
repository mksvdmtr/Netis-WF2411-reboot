import time
from selenium import webdriver
browser = webdriver.Firefox()
browser.minimize_window()
browser.get('http://username:password@x.x.x.x') #enter your username, password and ip address
time.sleep(2)
advance = browser.find_element_by_css_selector('#imgsrc')
advance.click()
time.sleep(2)
system = browser.find_element_by_css_selector('#p_menu_misc > div:nth-child(2)')
system.click()
system_reboot = browser.find_element_by_css_selector('#c_menu_reboot > div:nth-child(2)')
system_reboot.click()
time.sleep(1)
click_to_reboot = browser.find_element_by_css_selector('#reboot')
time.sleep(2)
click_to_reboot.click()
time.sleep(1)
alert = browser.switch_to.alert
alert.accept()
time.sleep(1)
browser.quit()
