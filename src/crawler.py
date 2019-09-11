from selenium import webdriver
from bs4 import BeautifulSoup
import urllib.request
import urllib.parse
import logging
import time

driver = webdriver.Chrome('./chromedriver')
url = "http://sogang.ac.kr/bachelor/students/notice/notice08.html"
driver.get(url)
time.sleep(10)
xpath = "/html/body/div/div"
element = driver.find_elements_by_css_selector("body > div > div")
#element = driver.find_element_by_xpath(xpath)
print(element.text)


'''
all_children_by_xpath = element.find_elements_by_xpath(".//*")
for child in all_children_by_xpath:
    print("new")
    print(type(child))
    print(child.text)

'''
#print("children : " + str(all_children_by_xpath))




# print("html : " + str(element.get_attribute('innerHTML')))

