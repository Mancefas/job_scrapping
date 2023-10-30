from commons import CV_BANKAS_URL, CV_LT_URL_START, CV_MARKET_URL_START, CV_ONLINE_URL_START
from is_url_valid import is_url_valid
from cv_bankas import scrape_jobs_cvBankas
from cv_lt import scrape_jobs_cvlt
from cv_market import scrape_jobs_cvmarket
from cv_online import scrape_jobs_cvonline


other_url = "https://otherwebsite.com"
not_a_url = "meuw"
looking_for_error = {"error": "bad adrress"}


def test_is_url_valid():
    assert is_url_valid(
        "https://www.cvbankas.lt/jobs/search/job_title/python/location/Vilnius") == True
    assert is_url_valid("some string") == False
    assert is_url_valid(666) == False


def test_cv_bankas():
    assert scrape_jobs_cvBankas(CV_BANKAS_URL) != []
    assert scrape_jobs_cvBankas(other_url) == []
    assert scrape_jobs_cvBankas(not_a_url) == looking_for_error


def test_cv_lt():
    assert scrape_jobs_cvlt(CV_LT_URL_START) != []
    assert scrape_jobs_cvlt(other_url) == []
    assert scrape_jobs_cvlt(not_a_url) == looking_for_error


def test_cv_market():
    assert scrape_jobs_cvmarket(CV_MARKET_URL_START) != []
    assert scrape_jobs_cvmarket(other_url) == []
    assert scrape_jobs_cvmarket(not_a_url) == looking_for_error


def test_cv_online():
    assert scrape_jobs_cvonline(CV_ONLINE_URL_START) != []
    assert scrape_jobs_cvonline(other_url) == []
    assert scrape_jobs_cvonline(not_a_url) == looking_for_error
