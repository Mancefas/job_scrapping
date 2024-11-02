import requests
from bs4 import BeautifulSoup


def scrape_job_in_cvlt(add_address):
    page = requests.get(add_address)
    soup = BeautifulSoup(page.content, "html.parser")

    job_description_container = soup.find(
        "div", class_="content job-description")
    text_blocks = job_description_container.find_all(["p", "li"])

    job_desc_string = ""

    for block in text_blocks:
        cleanedText = block.text.strip()
        if cleanedText:
            job_desc_string = job_desc_string + cleanedText

    return job_desc_string
