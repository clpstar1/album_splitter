import subprocess
import sys
import argparse
import comm_generation
import discogs


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
        track_data = comm_generation.trackdata_from_file(args.commfile, args.delim)
    
    comm_generation.run_ffmpeg(
            comm_generation.gen_ffmpeg_commands(
                args.audio_file,
                track_data,
                args.artist
            )
        )
