import os
import argparse

from get_lyrics import GetLyrics
from get_song import GetSongs

def check_dir(dir_name):
    check_dir = os.path.isdir(dir_name)
    if not check_dir:
        os.makedirs(dir_name)
    return None

def main(song_names:list,
         save_dir:str,
         langs:list = ['ta', 'eng'],
         only_lyrics:bool = False
         ):

    if only_lyrics == False:
        song_save_dir = os.path.join(save_dir, 'Songs')
        check_dir(song_save_dir)
        song_downloader = GetSongs(song_save_dir)
        song_downloader.download_songs(song_names)

    lyrics_save_dir = os.path.join(save_dir, 'Lyrics')
    check_dir(lyrics_save_dir)
    lyrics_fetcher = GetLyrics(save_dir=lyrics_save_dir)
    lyrics_fetcher.get_lyrics(song_names=song_names)
    

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--songs', help='specify song names to download #use , to separate multiple song names')
    parser.add_argument('--save_dir', help='Directory to save downloaded songs and lyrics')
    parser.add_argument('--lang', help='language to download the lyrics', default='ta,en')
    args = parser.parse_args()
    songs = args.songs.split(',')
    langs = args.lang.split(',')
    main(song_names=songs,
         save_dir=args.save_dir,
         langs=langs)
