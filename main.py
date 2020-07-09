import subprocess
import sys
import argparse
import ffmpeg
import parse

def setUpParser():
    parser = argparse.ArgumentParser()
    parser.add_argument('audio_file')

    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('--url')
    group.add_argument('--commfile')

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
        track_data = parse.commands_from_file(args.file, args.delim)
    
    ffmpeg.run_ffmpeg(
            ffmpeg.gen_ffmpeg_commands(
                args.audio_file,
                track_data,
                args.artist
            )
        )
