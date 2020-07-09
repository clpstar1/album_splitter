import subprocess
import sys
import argparse
from datetime import datetime, timedelta

ffmpeg_template_str = 'ffmpeg -i AUDIO_FILE -acodec copy -ss START_TIME -to END_TIME'

def commands_from_file(command_file, delim):
    # start at 00:00:00
    start = timedelta(hours=0, minutes=0, seconds=0)
    track_data = []
    
    with open(command_file) as file:
        ## read all those line 
        lines = file.readlines()
    
    for line in lines: 
        # strip off newline
        title, duration = line.rstrip('\n').split(delim)
        # split into minute and secs to build timedelta
        m, s = duration.split(":")
        duration_td = timedelta(minutes=int(m), seconds=int(s))
        # create a list of form [(title, start, end)]
        track_data.append(
            (
                title,
                str(start), 
                str(start + duration_td)
            )
        )
        # increment the start time to the fit the start time of the next song 
        start += duration_td
    print(track_data)
    return track_data
    
def gen_ffmpeg_commands(audio_file, track_data: list, artist):
    
    tmp = list(filter(lambda t_info : len(t_info) != 3, track_data))
    print(tmp)
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

def setUpParser():
    parser = argparse.ArgumentParser()
    parser.add_argument('audio_file')

    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('--url')
    group.add_argument('--file')

    parser.add_argument('--delim',
        default=','
    )
    parser.add_argument('--artist',
        default=''
    )
    return parser

if __name__ == '__main__':
    
    parser = setUpParser()
    args = parser.parse_args()
    
    # fetch from discogs, not implemented yet
    if args.url is not None:
        pass
    else:
        track_data = commands_from_file(args.file, args.delim)
    
    run_ffmpeg(
            gen_ffmpeg_commands(
                args.audio_file,
                track_data,
                args.artist
            )
        )
