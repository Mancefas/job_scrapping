import requests
import json
from bs4 import BeautifulSoup
from is_url_valid import is_url_valid


def scrape_jobs_cvonline(websiteName, deeperUrl="/lt/search?limit=20&offset=0&categories%5B0%5D=INFORMATION_TECHNOLOGY&fuzzy=true&suitableForRefugees=false&isHourlySalary=false&isRemoteWork=false&isQuickApply=false"):
    if not is_url_valid(websiteName):
        return {"error": "bad adrress"}

    URL = websiteName + deeperUrl
    page = requests.get(URL)

    soup = BeautifulSoup(page.content, "html.parser")
    jobs = soup.findAll("li", class_="vacancies-list__item")

    job_data_list = []

    for job in jobs:
        linkElement = job.find("a", class_="vacancy-item__title")
        link = websiteName + \
            linkElement.get("href") if linkElement.get(
                "href") is not None else None

        title = job.find("span", class_="vacancy-item__title").text if job.find(
            "span", class_="vacancy-item__title") is not None else None

        company = job.find("div", class_="vacancy-item__column").text if job.find(
            "div", class_="vacancy-item__column") is not None else None

        company_img = websiteName + job.find("img")["src"] if job.find(
            "img") is not None else None

        city = job.find("div", class_="vacancy-item__locations").text if job.find(
            "div", class_="vacancy-item__locations") is not None else None

        time_added = job.find("div", class_="vacancy-item__info-secondary").find(
            "span").text if job.find("div", class_="vacancy-item__info-secondary") is not None else None

        salary = job.find("span", class_="vacancy-item__salary-label").text if job.find(
            "span", class_="vacancy-item__salary-label") is not None else None

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
