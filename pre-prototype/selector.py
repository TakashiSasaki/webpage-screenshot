#!/usr/bin/python3
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument('--start-maximized')
chrome = webdriver.Chrome(chrome_options=chrome_options)
#chrome.manage().window().maximize()

import sys
if len(sys.argv) not in (3,4):
    raise RuntimeError("Expecting two arguments, URL and a path for the screenshot.")


import logging
logging.basicConfig(level=logging.INFO)

url = sys.argv[1]
logging.info(url)
path = sys.argv[2]
logging.info(path)

if len(sys.argv) > 3:
  css_selector = sys.argv[3]
else:
  css_selector = "body"
logging.info(css_selector)

chrome.get(url)
document_scroll_width = chrome.execute_script("return document.documentElement.scrollWidth;")
logging.info(document_scroll_width)
document_scroll_height = chrome.execute_script("return document.documentElement.scrollHeight;")
logging.info(document_scroll_height)
element = chrome.find_elements_by_css_selector(css_selector)
if isinstance(element, list):
    element = element[0]

chrome.set_window_size(document_scroll_width, document_scroll_height)
#body = chrome.find_element_by_tag_name('body')

with open(path, "wb") as file:
        file.write(element.screenshot_as_png)

