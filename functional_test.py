from selenium import webdriver
import time

try:
    browser = webdriver.Chrome()
    time.sleep(2)
    browser.get('http://127.0.0.1:8000/')
    assert 'Django' in browser.title
finally:
    time.sleep(2)
    browser.quit() 
