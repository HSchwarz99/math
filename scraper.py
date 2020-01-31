from ana_1 import ana_scraper
from lina_1 import lina_scraper
from coma_1 import coma_scraper

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
from bs4 import BeautifulSoup
import requests
import os
import sys

def get_session_cookies(userdata):
  '''
  description: gets the cookies of the website via loging in with selenium
  input: userdata in dict like {name: user_name, password: password}
  output: cookie dict with name of cookies as keys and values as values
  '''
  url = "https://isis.tu-berlin.de/auth/shibboleth/index.php"
  driver = webdriver.Chrome(ChromeDriverManager().install())
  driver.get(url)
  time.sleep(3)
  password = driver.find_element_by_css_selector("#password")
  name = driver.find_element_by_css_selector("#username")
  submit = driver.find_element_by_css_selector("#login-button")
  webdriver.common.action_chains.ActionChains(driver).click(name).send_keys(userdata["name"]).click(password).send_keys(userdata["password"]).click(submit).perform()
  cookies = driver.get_cookies()
  driver.quit()
  cookies_dict = dict()
  for c in cookies:
    cookies_dict[c["name"]] = c["value"]
  return cookies_dict


def execute_all_scrapers(scrapers):
  '''
  description: executes all scrapers in list
  input: scraper list
  output: None
  '''
  u_data = dict()
  for x in open("ENV", "r").read().split("\n"):
    if len(x) > 0:
      y = x.split("=")
      u_data[y[0]] = y[1]
  C = get_session_cookies(u_data)
  path = os.path.abspath(os.path.dirname(sys.argv[0]))
  for s in scrapers:
    s.execute_scraper(C, path)

S = [ana_scraper, lina_scraper, coma_scraper]
execute_all_scrapers(S)
