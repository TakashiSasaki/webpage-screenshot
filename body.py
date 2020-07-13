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
if len(sys.argv) != 3:
    raise RuntimeError("Expecting two arguments, URL and a path for the screenshot.")


import logging
logging.basicConfig(level=logging.INFO)

url = sys.argv[1]
logging.info(url)
path = sys.argv[2]
logging.info(path)

chrome.get(url)
documentScrollWidth = chrome.execute_script("return document.documentElement.scrollWidth;")
logging.info(documentScrollWidth)
documentScrollHeight = chrome.execute_script("return document.documentElement.scrollHeight;")
logging.info(documentScrollHeight)
chrome.set_window_size(documentScrollWidth, documentScrollHeight)
body = chrome.find_element_by_tag_name('body')

with open(path, "wb") as file:
        file.write(body.screenshot_as_png)

