from selenium import webdriver
from bs4 import BeautifulSoup
import urllib.request
import urllib.parse
import logging
import time
#logger = logging.getLogger(__name__)
logger = logging.getLogger("")
logger.setLevel(logging.INFO)

driver = webdriver.Chrome('./chromedriver')
url = "http://scc.sogang.ac.kr/front/cmsboardlist.do?siteId=cs&bbsConfigFK=1745"
driver.get(url)
time.sleep(10)
xpath = "//*[@id='body']/div[2]/div[4]/div/div"
#elements = driver.find_elements_by_tag_name("a")
element = driver.find_element_by_xpath(xpath)
#print((element.get_attribute('innerHTML')))
#logger.info("efefefefefefef")
#print((element.get_attribute('outerHTML')))
print(element.text)
'''
all_children_by_xpath = element.find_elements_by_xpath("*")
for child in all_children_by_xpath:
    print("new")
    print(type(child))
    print(child.text)
'''

#print("children : " + str(all_children_by_xpath))
# print("html : " + str(element.get_attribute('innerHTML')))

