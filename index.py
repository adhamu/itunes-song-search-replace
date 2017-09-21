#!/usr/bin/env python3

import pickle
import os
import time
from mutagen.easyid3 import EasyID3
from libpytunes import Library
import argparse


def update(song):
    """Update song name via it's ID3 tag."""
    try:
        audio = EasyID3('/' + song.location)
        audio['title'] = song.name.replace(offence, replace_offence_with)
        audio.save()
        print('Saved as ' + audio['title'][0])
    except Exception:
        print('File not found. Try clearing your cache')

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Searches your iTunes library and replaces an offending string'
    )
    parser.add_argument(
        '-i',
        metavar='iTunes Library',
        type=str,
        required=True,
        help='Absolute path to iTunes Library XML file'
    )
    parser.add_argument(
        '-s',
        metavar='Search term',
        type=str,
        required=True,
        help='The string you are searching for'
    )
    parser.add_argument(
        '-r',
        metavar='Replace with',
        type=str,
        required=True,
        help='What you want to replace it with'
    )
    parser.add_argument(
        '--nocache',
        action='store_true',
        help='Disable caching with pickle'
    )
    parser.add_argument(
        '--noconfirm',
        action='store_true',
        help='Don\'t confirm changes, just apply to all results'
    )

    args = parser.parse_args()

    itunes_library = os.path.realpath(args.i)
    offence = args.s
    replace_offence_with = args.r
    confirm_message = 'Replace "' + offence + '" with ' + '"' + replace_offence_with + '" [y/n] ? '
    found = False

    lib_path = itunes_library
    pickle_file = 'itl.p'
    expiry = 0 if args.nocache else (60 * 60)
    epoch_time = int(time.time())

    if not os.path.isfile(pickle_file) or os.path.getmtime(pickle_file) + expiry < epoch_time:
        itl_source = Library(lib_path)
        pickle.dump(itl_source, open(pickle_file, 'wb'))

    itl = pickle.load(open(pickle_file, 'rb'))

    for id, song in itl.songs.items():
        if song.name.find(offence) != -1:
            found = True
            print('/' + song.location)

            if args.noconfirm:
                update(song)
            else:
                confirmation = input(confirm_message)
                if confirmation == 'y':
                    update(song)
                else:
                    print('Song name not changed')

    if found is False:
        print('No results found')
