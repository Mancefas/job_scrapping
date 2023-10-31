import requests
import json
from bs4 import BeautifulSoup
from is_url_valid import is_url_valid


def scrape_jobs_cvlt(websiteName, deeperUrl="/it-telekomunikaciju-darbai"):
    if not is_url_valid(websiteName + deeperUrl):
        return {"error": "bad adrress"}

    URL = websiteName + deeperUrl
    page = requests.get(URL)

    soup = BeautifulSoup(page.content, "html.parser")
    jobs = soup.findAll("div", {"data-ng-if": "bulletins.first"})

    job_data_list = []

    for job in jobs:
        # if item has a form it is not a job
        hasForm = job.find("form")
        if hasForm:
            break

        linkComponent = job.find(class_="job-wr")
        link = websiteName + \
            linkComponent.get("href") if linkComponent is not None else None

        title = job.find(class_="title").text if job.find(
            class_="title") is not None else None

        company = job.find("span", class_="company").text if job.find(
            "span", class_="company") is not None else None

        company_img = websiteName + job.find("div", class_="img-wr").find(
            "img")["src"] if job.find("div", class_="img-wr") is not None else None

        city = job.find("span", class_="company").find("span", class_=False).text if job.find(
            "span", class_="company") is not None else None

        time_added = job.find("div", class_="options-wr").text if job.find(
            "div", class_="options-wr") is not None else None

        salary = job.find("span", class_="salary").text if job.find(
            "span", class_="salary") is not None else None

        job_data = {
            "link": link,
            "title": title,
            "company": company,
            "company_img": company_img,
            "city": city,
            "time_added": time_added,
            "salary": salary
        }

        job_data_list.append(job_data)

    return json.dumps(job_data_list)
