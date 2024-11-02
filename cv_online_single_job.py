import requests
from bs4 import BeautifulSoup
import json


def scrape_job_in_cvonline(add_address):
    # page = requests.get(add_address)
    # soup = BeautifulSoup(page.content, "html.parser")

    # job_description_container = soup.find(
    #     "div", id="react-tabs-1")
    # text_blocks = soup.find_all(["p", "li"])

    # job_desc_string = ""

    # for block in text_blocks:
    #     cleanedText = block.text.strip()
    #     if cleanedText:
    #         job_desc_string = job_desc_string + cleanedText
    # print(job_description_container)
    # return job_desc_string
    return json.dumps("not working while figuring out ")
