from urllib.parse import urlparse
import requests
from util import gen_timedeltas

def trackdata_from_discogs(url):

    # parse the url and extrac the release number
    parsed_url = urlparse(url)
    if parsed_url.netloc != 'www.discogs.com':
        raise ValueError("unsupported URL: hostname is not of type www.discogs.com")

    release_num = parsed_url.path.split('/')[-1]

    # prepare the request
    response = \
        requests.get(
            'https://api.discogs.com/releases/' + release_num
            , headers={'user-agent' : 'tracklistfetcher/0.1'}
            )
    
    # raise http error if unsuccesful
    response.raise_for_status()

    return parse_response(response.json())

def parse_response(response):
    
    tracklist = response["tracklist"]

    titles = (tr["title"] for tr in tracklist)
    durations = (tr["duration"] for tr in tracklist)
    
    timedeltas = gen_timedeltas(durations)
    # join together two lists of form:
    # - ["title1", "title2"...] 
    # - [("start1, end1", "start2, end2")]
    # -> [("title1, start1, end1"), ("title2, start2, end2")]
    return [(ti,) + td for ti, td in zip (titles, timedeltas)]
