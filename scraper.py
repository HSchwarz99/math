from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
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
  options = Options()
  options.add_argument("--headless")
  driver = webdriver.Chrome(options=options)
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

def scrape_list(m_id, document_list, cookies):
  '''
  description: gets list of document ids from modulepage on isis
  input: modulepage id, document list, cookies
  output: dict with key as document type and values as list of sections with
  sublist of items with [name, id]
  '''
  url = "https://isis.tu-berlin.de/course/view.php?id=" + m_id
  page = BeautifulSoup(requests.get(url, cookies=cookies).text, 'html.parser')
  sections = page.select("li.section")
  for s in page.select("span.instancename span.accesshide"):
    s.decompose()
  return_dict = dict()
  for d_type in document_list:
    return_dict[d_type] = []
    for section in sections:
      return_dict[d_type].append([[x.select(".instancename")[0].text, x.select("a")[0]["href"]] for x in section.select(".modtype_" + d_type)])
  return return_dict

def prepare_dir(document_type):
  '''
  description: makes sure there is a diretory for the document type and creates
  one if there is not
  input: document type name
  output: None
  '''
  os.system("if [ ! -d " + document_type + " ];then\nmkdir " + document_type + "\nfi")


def update_dir(document_type, document_list, cookies):
  '''
  description: updates the contents of a dir and calls functions to scrape files
  into the intended location
  input: document type, scraped list with documnts on website
  output: None
  '''
  os.chdir(document_type)
  files = os.listdir()
  for section in document_list:
    for x in section:
      if x[0].translate(str.maketrans({"/": "|"})) not in files:
        get_pdf(x[0], x[1], cookies)
  os.chdir("..")

def get_pdf(name, view_id, cookies):
  '''
  description: downloads pdf from website and saves them
  input: name, id of pdf
  output: None
  '''
  url = view_id
  file = requests.get(url, allow_redirects=True, cookies=cookies)
  open(name.translate(str.maketrans({"/": "|"})), "wb").write(file.content)

def execute_scraper(cookies, path, mod_dict):
  '''
  description: executes the scraper for one module
  input: cookies, path to the math directory, and the mod dict
  output: None
  '''
  cwd = os.getcwd()
  os.chdir(path + mod_dict["path"])
  L = scrape_list(mod_dict["page_id"], mod_dict["d_list"], cookies)
  for s in mod_dict["d_list"]:
    prepare_dir(s)
    update_dir(s, L[s], cookies)
  os.chdir(cwd)


def execute_all_scrapers(L):
  '''
  description: executes all scrapers in list
  input: scraper list
  output: None
  '''
  u_data = dict()
  path = os.path.abspath(os.path.dirname(sys.argv[0]))
  for x in open(path + "/ENV", "r").read().split("\n"):
    if len(x) > 0:
      y = x.split("=")
      u_data[y[0]] = y[1]
  C = get_session_cookies(u_data)
  for l in L:
    execute_scraper(C, path, l)

ana_dict = {"path": "/ana_1",
"d_list": ["quiz", "resource"],
"page_id": "17453"
}
lina_dict = {"path": "/lina_1",
"d_list": ["resource"],
"page_id": "16999"
}
coma_dict = {"path": "/coma_1",
"d_list": ["resource"],
"page_id": "17195"
}
S = [ana_dict, lina_dict, coma_dict]
execute_all_scrapers(S)
