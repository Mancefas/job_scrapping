import requests
from bs4 import BeautifulSoup


def scrape_jobs_cvBankas():
    URL = "https://www.cvbankas.lt/?padalinys%5B%5D=76&keyw="
    page = requests.get(URL)

    soup = BeautifulSoup(page.content, "html.parser")
    jobs = soup.findAll(class_="list_a")

    object_for_json = []

    for job in jobs:
        link = job.get("href") if job.get("href") is not None else None
        title = job.find(class_="list_h3").text if job.find(
            class_="list_h3") is not None else None
        company = job.find("span", class_="dib").text if job.find(
            "span", class_="dib") is not None else None
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
            "city": city,
            "time_added": time_added,
            "salary": salary
        }

        object_for_json.append(job_data)

    return object_for_json
