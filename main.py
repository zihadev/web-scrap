# coding=utf-8
import requests
import selectorlib
from selectorlib import Extractor
import time

URL = "http://programmer100.pythonanywhere.com/tours/"


def scrape(url):
    """Scrapes source of url"""
    response = requests.get(url)
    html_content = response.text  # Renamed to avoid potential shadowing
    return html_content


def extract_timer(html_source):
    """Extracts the timer data from the HTML source"""
    extractor = Extractor.from_yaml_string("""
    timer:
       css: 'h1#displaytimer'
       xpath: null
       type: Text
    """)

    timer_data = extractor.extract(html_source)[
        'timer']  # Used a more specific name
    return timer_data


def saving_data(data):
    # Get the current local time
    current_time = time.localtime()

    # Format the time to show date and hour
    formatted_time = time.strftime("%Y-%m-%d %H:%M:%S", current_time)
    with open("concerts.txt", "r") as file:
        notes = file.read()
    with open("concerts.txt", "a") as file:
        if data in notes:

            print("already is")
        else:
            file.write(f"{data}  -- [checked and saved: {formatted_time}]\n")


if __name__ == "__main__":
    scraped_content = scrape(
        URL)  # Renamed to avoid shadowing with any outer scope
    result = extract_timer(scraped_content)
    saving_data(result)
    print(result)
