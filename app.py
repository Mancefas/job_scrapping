from flask import Flask
from flask_cors import CORS
from commons import CV_BANKAS_URL, CV_LT_URL_START, CV_LT_URL_DEEPER, CV_MARKET_URL_START, CV_MARKET_URL_DEEPER, CV_ONLINE_URL_START, CV_ONLINE_URL_DEEPER
from cv_bankas import scrape_jobs_cvBankas
from cv_lt import scrape_jobs_cvlt
from cv_market import scrape_jobs_cvmarket
from cv_online import scrape_jobs_cvonline
from cv_bankas_single_job import scrape_job_in_cvbankas
from ask_AI import ask_ai

app = Flask(__name__)
CORS(app)


def main():
    app.run(host='0.0.0.0', port=5000, debug=True)


@app.route("/")
def home():
    return "<h1>hello there</h1>"


@app.route("/cvbankas")
def cv_bankas():
    return scrape_jobs_cvBankas(CV_BANKAS_URL)


@app.route("/cvbankas/<path:url>")
def one_job(url):
    return ask_ai(scrape_job_in_cvbankas(url))


@app.route("/cvlt")
def cv_lt():
    return scrape_jobs_cvlt(CV_LT_URL_START, CV_LT_URL_DEEPER)


@app.route("/cvmarket")
def cv_market():
    return scrape_jobs_cvmarket(CV_MARKET_URL_START, CV_MARKET_URL_DEEPER)


@app.route("/cvonline")
def cv_online():
    return scrape_jobs_cvonline(CV_ONLINE_URL_START, CV_ONLINE_URL_DEEPER)


if __name__ == "__main__":
    main()
