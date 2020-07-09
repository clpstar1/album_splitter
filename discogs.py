from urllib.parse import urlparse
import requests

def fetch_trackdata(url):

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


def parse_response(response):
    pass
