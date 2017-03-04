import argparse

parser = argparse.ArgumentParser(add_help=True, description='search swagbucks')

parser.add_argument('-t', action='store', default=60,
                    help='timeout on a search and earn')
parser.add_argument('-vf', action='store', default='data/playlists.txt',
                    help='Where to store video list')
parser.add_argument('-m', action='store_true', default=False,
                    help='sort by time/SB, default sorts by video count/SB')

parser.add_argument('--version', action='version', version='%(prog)s 1.0')

args = parser.parse_args()