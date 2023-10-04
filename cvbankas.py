import requests
from bs4 import BeautifulSoup

URL = "https://www.cvbankas.lt/?padalinys%5B%5D=76&keyw="
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")
jobs = soup.findAll(class_="list_a")

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
