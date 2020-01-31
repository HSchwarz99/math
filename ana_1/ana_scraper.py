import requests
from bs4 import BeautifulSoup
import os

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

def execute_scraper(cookies, path_to_math):
  '''
  description: executes the scraper
  input: cookies and the path to the math dir
  output: None
  '''
  cwd = os.getcwd()
  os.chdir(path_to_math + "/ana_1")
  d_list = ["quiz", "resource"]
  anapage_id = "17453"
  L = scrape_list(anapage_id, d_list, cookies)
  for d in d_list:
    prepare_dir(d)
    update_dir(d, L[d], cookies)
  os.chdir(cwd)
