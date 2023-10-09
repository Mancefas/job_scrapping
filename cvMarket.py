import requests
from bs4 import BeautifulSoup


def scrape_jobs_cvmarket():
    websiteName = "https://www.cvmarket.lt"
    URL = websiteName + "/darbo-skelbimai?op=search&search%5Bjob_salary%5D=3&ga_track=homepage&search%5Bcategories%5D%5B%5D=8&search%5Bkeyword%5D=&search%5Bexpires_days%5D=&search%5Bjob_lang%5D=&search%5Bsalary%5D="
    page = requests.get(URL)

    soup = BeautifulSoup(page.content, "html.parser")
    jobs = soup.findAll("article", {"data-component": "jobad"})

    job_data_list = []

    for job in jobs:
        linkTag = job.find(class_="jobad-url")
        link = websiteName + \
            linkTag.get("href") if linkTag.get("href") is not None else None

        title = job.find("h2").text if job.find("h2") is not None else None

        company = job.find("span", class_="job-company").text if job.find(
            "span", class_="job-company") is not None else None

        city = job.find("span", class_="location").find("div", class_=False).text if job.find(
            "span", class_="location") is not None else None

        time_added = job.find("span", class_=False).text if job.find(
            "span", class_=False) is not None else None

        salaryBlock = job.find("div", class_="salary-block")
        salary = salaryBlock.find("span").text if job.find(
            "span") is not None else None

        job_data = {
            "link": link,
            "title": title,
            "company": company,
            "city": city,
            "time_added": time_added,
            "salary": salary
        }

        job_data_list.append(job_data)

    return job_data_list
