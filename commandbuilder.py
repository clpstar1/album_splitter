import subprocess
from util import gen_timedeltas, run_ffmpeg


class FFMPEGBuilder():

    def __init__(self, retriever, audio_file, out_dir='.'):
        self.retriever = retriever
        self.audio_file = audio_file
        self.out_dir = out_dir
        # use extension of the original file
        self.out_format = self.audio_file.split(".")[-1]

        self.template_str = 'ffmpeg -i AUDIO_FILE -acodec copy -ss START_TIME -to END_TIME OUTPUT_DIR/FILE.EXTENSION'
    

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
        map_lambda = lambda entry : map_entries(entry)
        for title, start, end in track_data:

            def map_entries(entry):
                if      entry   == "START_TIME" : return start 
                elif    entry   == "END_TIME"   : return end
                elif    entry   == "AUDIO_FILE" : return self.audio_file
                elif    entry.startswith("OUTPUT_DIR"): 
                    return self.out_dir + "/" + title + "." + self.out_format
                else: return entry

            tmp = list(map(map_lambda, self.template_str.split(" ")))
            print(tmp)
            ffmpeg_commands.append(
                tmp
            )

        return ffmpeg_commands
    
