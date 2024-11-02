import requests
from bs4 import BeautifulSoup
import json


def scrape_job_in_cvmarket(add_address):
    page = requests.get(add_address)
    soup = BeautifulSoup(page.content, "html.parser")

    iframe = soup.find('iframe', id='htmlContentIframe')
    iframe_soup = BeautifulSoup(str(iframe), 'html.parser')

    job_description_elements = iframe_soup.find_all('p')

    job_description = ""
    for p in job_description_elements:
        job_description += p.get_text(strip=True)

    # print(iframe_soup)
    # return job_description
    return json.dumps("not working while figuring out iframe")
