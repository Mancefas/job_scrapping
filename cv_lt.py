import requests
import json
from bs4 import BeautifulSoup
from is_url_valid import is_url_valid


def scrape_jobs_cvlt(websiteName, deeperUrl="/jobs?search%5Bcategories%5D%5B%5D=8"):
    if not is_url_valid(websiteName + deeperUrl):
        return {"error": "bad adrress"}

    URL = websiteName + deeperUrl
    page = requests.get(URL)

    soup = BeautifulSoup(page.content, "html.parser")
    jobs = soup.findAll("article", {"data-component": "jobad"})

    job_data_list = []

    for job in jobs:
        # if item has a form it is not a job
        hasForm = job.find("form")
        if hasForm:
            break

        linkComponent = job.find(class_="block nohover")
        link = websiteName + \
            linkComponent.get("href") if linkComponent is not None else None

        title = job.find("h2").text if job.find(
            "h2") is not None else None

        company = job.find("div", class_="job-company").text if job.find(
            "div", class_="job-company") is not None else None

        company_img = job.find("div", class_="logo-block").find(
            "img")["src"] if job.find("div", class_="logo-block") is not None else None

        city = job.find("span", class_="job-location").text if job.find(
            "span", class_="job-location") is not None else None

        time_added = job.find("div", class_="text-sm lg:text-base text-stone-600 whitespace-nowrap").text if job.find(
            "div", class_="text-sm lg:text-base text-stone-600 whitespace-nowrap") is not None else None

        salaryHolder = job.find("span", {"data-component": "badge"})

        salary = salaryHolder.find("div").text if salaryHolder is not None else None

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
