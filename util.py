from datetime import datetime, timedelta
import subprocess

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