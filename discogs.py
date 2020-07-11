from urllib.parse import urlparse
import requests
from retrieverbase import RetrieverBase
from util import gen_timedeltas, uniquify

class DiscogsRetriever(RetrieverBase):

    def __init__(self, data_source):
        super().__init__(data_source)
    
    def retrieve_trackdata(self):
        # parse the url and extrac the release number
        parsed_url = urlparse(self.data_source)
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

        return self.parse_response(response.json())

    def parse_response(self, response):
        
        tracklist = response["tracklist"]

        if tracklist is None:
            raise ValueError("Could not find \"tracklist\" entry in http reponse")

        titles = (tr["title"] for tr in tracklist)
        durations = (tr["duration"] for tr in tracklist)
        
        return super().gen_commands(titles, durations)