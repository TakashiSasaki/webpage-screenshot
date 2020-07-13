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

url = sys.argv[1]
logging.info(url)
path = sys.argv[2]
logging.info(path)

chrome.get(url)
chrome.save_screenshot(path)

