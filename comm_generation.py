import subprocess
from util import gen_timedeltas, run_ffmpeg

ffmpeg_template_str = 'ffmpeg -i AUDIO_FILE -acodec copy -ss START_TIME -to END_TIME'

class FFMPEGBuilder():

    def __init__(self, retriever, audio_file):
        self.retriever = retriever
        self.audio_file = audio_file
    
    def run(self):
        track_data = self.retriever.retrieve_trackdata()
        ffmpeg_comms = self.gen_ffmpeg_commands(track_data)
        run_ffmpeg(ffmpeg_comms)

    def gen_ffmpeg_commands(self, track_data):
        
        tmp = list(filter(lambda t_info : len(t_info) != 3, track_data))
        if len(tmp) > 0:
            raise ValueError(
        "track_data must contain exactly three String values per Entry: title, start, end"
        )

        # create commands for ffmpeg 
        ffmpeg_commands = []
        for title, start, end in track_data:
            tmp = ffmpeg_template_str
            tmp =\
                tmp\
                    .replace("START_TIME", start)\
                    .replace("END_TIME", end)\
                    .split(" ") + [title + '.mp3']
                    # ^ plus is needed to return a new list
                    # and needs to occur after split since
                    # else it would split the filename if it contains any
                    # spaces. 
                    # could also be shifted to .append since i need
                    # to insert afterwards anyways but im too lazy right now
                    # (i couldve probably done it already while writing this bullshit lol)
            tmp[2] = self.audio_file
            ffmpeg_commands.append(tmp)
        
        return ffmpeg_commands
            
