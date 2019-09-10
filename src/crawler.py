from selenium import webdriver
from bs4 import BeautifulSoup
import urllib.request
import urllib.parse
import logging

driver = webdriver.Chrome('./chromedriver')
url = "http://sogang.ac.kr/bachelor/students/notice/notice08.html"
xpath = "//*[@id='mainFrm']"

driver.get(url)
element = driver.find_element_by_xpath(xpath)
print(element.get_attribute('outerHTML'))