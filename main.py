import requests
import selectorlib
from selectorlib import Extractor
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# URL = "http://programmer100.pythonanywhere.com/tours/"
URL = "https://www.onet.pl/"


def scrape(url):
    """Scrapes source of url"""
    response = requests.get(url)
    source1 = response.text
    return source1


def scrape_js(url):
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(url)
    title = driver.title
    source2 = driver.page_source
    print('title: ', title)
    print('source: \n', source2)
    driver.quit()
    return title, source2


def yaml_timer(source):
    """Scrapes the data from the scrapped url"""
    extractor = Extractor.from_yaml_string("""
    timer:
       css: 'h1#displaytimer'
       xpath: null
       type: Text
    """)

    data = extractor.extract(source)['timer']
    return data


if __name__ == "__main__":
    source = (scrape(URL))
    print(yaml_timer(source))
    print(5 * '*')
    print(scrape_js(URL))
