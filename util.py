from datetime import datetime, timedelta
import subprocess
from collections import Counter

# format ["mm:ss", "mm:ss"]
def gen_timedeltas(durations, delim=':'):
    start = timedelta(hours=0, minutes=0, seconds=0)
    deltas = []
    for d in durations:
        # split into minute and secs to build timedelta
        m, s = d.split(delim)
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

def run_ffmpeg(ffmpeg_commands):
        for command in ffmpeg_commands:
            subprocess.call(command)


# credit: https://stackoverflow.com/questions/30650474/python-rename-duplicates-in-list-with-progressive-numbers-without-sorting-list
def uniquify(str_list):
    """
    AutoIndex Strings that occur > 1 in a List of Strings
    ["a", "b", "b"] -> ["a", "b1", "b2"]
    """
    counts = {k:v for k,v in Counter(str_list).items() if v > 1}
    newlist = str_list[:]

    for i in reversed(range(len(str_list))):
        item = str_list[i]
        if item in counts and counts[item]:
            newlist[i] += str(counts[item])
            counts[item]-=1
    
    return newlist