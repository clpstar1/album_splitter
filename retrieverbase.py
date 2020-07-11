from util import gen_timedeltas, uniquify

class RetrieverBase():

    def __init__(self, data_source):
        self.data_source = data_source
    
    def retrieve_trackdata(self, data_source):
        pass

    def gen_commands(self, titles, durations):
        timedeltas = gen_timedeltas(durations)
        # join together two lists of form:
        # - ["title1", "title2"...] 
        # - [("start1, end1", "start2, end2")]
        # -> [("title1, start1, end1"), ("title2, start2, end2")]
        return [(ti,) + td for ti, td in zip (uniquify(list(titles)), timedeltas)]

class FileRetriever(RetrieverBase):

    def __init__(self, data_source, delim):
        super().__init__(data_source)
        self.delim = delim 

    def retrieve_trackdata(self):
        with open(self.data_source) as file:
            lines = file.readlines()
        
        # remove newlines and split on delim
        de_newlined = [line.rstrip('\n').split(self.delim) for line in lines]
        
        # generator-expressions for lazy eval
        titles = (td_pair[0] for td_pair in de_newlined)
        durations = (td_pair[1] for td_pair in de_newlined)
        
        return super().gen_commands(titles, durations)
