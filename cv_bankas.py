import requests
import json
from bs4 import BeautifulSoup
from is_url_valid import is_url_valid


def scrape_jobs_cvBankas(url: str):
    if not is_url_valid(url):
        return {"error": "bad adrress"}

    page = requests.get(url)

    soup = BeautifulSoup(page.content, "html.parser")
    jobs = soup.findAll(class_="list_a")

    object_for_json = []

    for job in jobs:
        link = job.get("href") if job.get("href") is not None else None
        title = job.find(class_="list_h3").text if job.find(
            class_="list_h3") is not None else None
        company = job.find("span", class_="dib").text if job.find(
            "span", class_="dib") is not None else None
        company_img = job.find("div", class_="list_logo_c").find(
            "img")["src"] if job.find("div", class_="list_logo_c") is not None else None
        city = job.find("span", class_="list_city").text if job.find(
            "span", class_="list_city") is not None else None
        time_added = job.find("span", class_="txt_list_2").text if job.find(
            "span", class_="txt_list_2") is not None else None
        salary = job.find("span", class_="salary_amount").text if job.find(
            "span", class_="salary_amount") is not None else None

        job_data = {
            "link": link,
            "title": title,
            "company": company,
            "company_img": company_img,
            "city": city,
            "time_added": time_added,
            "salary": salary,
        }

        object_for_json.append(job_data)

    return json.dumps(object_for_json)
