#!/usr/bin/python3
class Driver():
    def __init__(self):
        from selenium import webdriver
        from selenium.webdriver.chrome.options import Options
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
        chrome_options.add_argument('--start-maximized')
        self.driver = webdriver.Chrome(chrome_options=chrome_options, keep_alive=True)

    def getElement(self, url, css_selector):
        self.driver.get(url)
        document_scroll_width = self.driver.execute_script("return document.documentElement.scrollWidth;")
        document_scroll_height = self.driver.execute_script("return document.documentElement.scrollHeight;")
        self.driver.set_window_size(document_scroll_width, document_scroll_height)
        element = self.driver.find_elements_by_css_selector(css_selector)
        if isinstance(element, list):
            return element[0]
        else:
            return element

    def getPng(self, url, css_selector):
        element = self.getElement(url, css_selector)
        return element.screenshot_as_png

    def savePng(self, url, css_selector, path):
        png = self.getPng(url, css_selector)
        with open(path, "wb") as file:
            file.write(png)

    def __del__(self):
        self.driver.close()
        self.driver.quit()

if __name__ == "__main__":
    url = "https://www.tenki.jp/" 
    path = "Driver.png"
    css_selector = "div#forecast-map-wrap"
    driver = Driver()
    driver.savePng(url, css_selector, path)
    #driver.driver.close()
    #driver.driver.quit()
