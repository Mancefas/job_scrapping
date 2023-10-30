from urllib.parse import urlparse


def is_url_valid(url):
    try:
        o = urlparse(url)
        if o.scheme and o.hostname:
            return True
        else:
            return False
    except:
        return False
