import requests
from bs4 import BeautifulSoup
import json


def scrape_job_in_cvbankas(add_address):
    page = requests.get(add_address)
    soup = BeautifulSoup(page.content, "html.parser")

    job_desc_string = ''
    skip_with_words = ["€/mėn", "€/mon."]

    job_full_descriptions = soup.select("[itemprop='description']")[
        0].findAll("div", class_="jobad_txt")

    for requermnt in job_full_descriptions:
        # clean text by removing whitespace, deleting new row(\n) and return(\r)
        cleaned_text = requermnt.text.strip().replace('\n', '').replace('\r', '')
        if not cleaned_text or any(word in cleaned_text for word in skip_with_words):
            continue
        else:
            job_desc_string = job_desc_string + cleaned_text

    print(job_desc_string)

    return job_desc_string
