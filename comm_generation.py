import subprocess
from datetime import datetime, timedelta

ffmpeg_template_str = 'ffmpeg -i AUDIO_FILE -acodec copy -ss START_TIME -to END_TIME'

def trackdata_from_file(command_file, delim):
    with open(command_file) as file:
        ## read all those line 
        lines = file.readlines()
    
    # remove newlines lazy, and split on delim
    de_newlined = [line.rstrip('\n').split(delim) for line in lines]
    
    # generator-expressions for lazy eval
    titles = (td_pair[0] for td_pair in de_newlined)
    durations = (td_pair[1] for td_pair in de_newlined)
    
    timedeltas = gen_timedeltas(durations)
    
    # join together two lists of form:
    # - ["title1", "title2"...] 
    # - [("start1, end1", "start2, end2")]
    # -> [("title1, start1, end1"), ("title2, start2, end2")]
    return [(ti,) + td for ti, td in zip (titles, timedeltas)]

# format ["mm:ss", "mm:ss"]
def gen_timedeltas(durations):
    start = timedelta(hours=0, minutes=0, seconds=0)
    deltas = []
    for d in durations:
        # split into minute and secs to build timedelta
        m, s = d.split(":")
        duration_td = timedelta(minutes=int(m), seconds=int(s))
        end = start + duration_td
        deltas.append(
                (
                    str(start)
                    , str(end)
                )
            )
        # increment the start time to the fit the start time of the next song 
        start += duration_td
    return deltas

def gen_ffmpeg_commands(audio_file, track_data: list, artist):
    
    tmp = list(filter(lambda t_info : len(t_info) != 3, track_data))
    if len(tmp) > 0:
        raise ValueError("track_data must contain exactly three values: title, start, end")

    # create commands for ffmpeg 
    ffmpeg_commands = []
    for title, start, end in track_data:
        tmp = ffmpeg_template_str
        tmp =\
            tmp\
                .replace("START_TIME", start)\
                .replace("END_TIME", end)\
                .split(" ") + [artist + ' - ' + title + '.mp3']
                # ^ plus is needed to return a new list
                # and needs to occur after split since
                # else it would split the filename if it contains any
                # spaces. 
                # could also be shifted to .append since i need
                # to insert afterwards anyways but im too lazy right now
                # (i couldve probably done it already while writing this bullshit lol)
        tmp[2] = audio_file
        ffmpeg_commands.append(tmp)
    
    return ffmpeg_commands
        
def run_ffmpeg(ffmpeg_commands):
    
    for command in ffmpeg_commands:
        subprocess.call(command)
