from flask import Flask, request
from cv_bankas import scrape_jobs_cvBankas
from cvLT import scrape_jobs_cvlt
from cvMarket import scrape_jobs_cvmarket
from cvOnline import scrape_jobs_cvonline

app = Flask(__name__)


@app.route("/")
def home():
    return "<h1>hello there</h1>"


@app.route("/cvbankas")
def cv_bankas():
    return scrape_jobs_cvBankas()


@app.route("/cvlt")
def cv_lt():
    return scrape_jobs_cvlt()


@app.route("/cvmarket")
def cv_market():
    return scrape_jobs_cvmarket()


@app.route("/cvonline")
def cv_online():
    return scrape_jobs_cvonline()


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
