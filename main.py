import subprocess
import sys
import argparse
from comm_generation import FFMPEGBuilder
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
        FFMPEGBuilder(DiscogsRetriever(args.url), args.audio_file).run()
    else:
        FFMPEGBuilder(FileRetriever(args.commfile, args.delim), args.audio_file).run()
    