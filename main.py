import subprocess
import sys
import argparse
import comm_generation
from base import FileRetriever
from discogs import DiscogsRetriever


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
    
    if args.url is not None:
        track_data = DiscogsRetriever().retrieve_trackdata(args.url)
    else:
        track_data = FileRetriever(args.delim).retrieve_trackdata(args.commfile)
    
    comm_generation.run_ffmpeg(
            comm_generation.gen_ffmpeg_commands(
                args.audio_file,
                track_data,
                args.artist
            )
        )
