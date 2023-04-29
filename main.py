import os
import argparse
import sys
from get_lyrics import GetLyrics
from get_song import GetSongs
# from spleeter import spleeter
import pandas as pd


def check_dir(dir_name):
    check_dir = os.path.isdir(dir_name)
    if not check_dir:
        os.makedirs(dir_name)
    return None

def main(song_df:pd.DataFrame,
         save_dir:str,
         langs:list = ['ta', 'eng'],
         only_lyrics:bool = False
         ):
    df = song_df
    song_names = df['Song'].tolist()
    
    if not os.path.isdir(save_dir):
        lyrics_save_dir = os.path.join(save_dir, 'Lyrics')
        check_dir(lyrics_save_dir)
        song_save_dir = os.path.join(save_dir, 'Songs')
        check_dir(song_save_dir)
    else:
        lyrics_save_dir = f'{save_dir}\\Lyrics'
        song_save_dir = f'{save_dir}\\Songs'
    for song in song_names:
        if only_lyrics == False:
            lyrics_fetcher = GetLyrics(save_dir=lyrics_save_dir)
            lyrics_fetcher.get_lyrics(song)
            song_downloader = GetSongs(song_save_dir)
            song_downloader.download_songs(song)

    # spleeter()
    
    
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--songs', help='specify song names to download #use , to separate multiple song names')
    parser.add_argument('--save_dir', help='Directory to save downloaded songs and lyrics')
    parser.add_argument('--lang', help='language to download the lyrics', default='ta,en')
    args = parser.parse_args()
    songs = args.songs.split(',')
    csv = sys.argv[2]
    df = pd.read_csv(csv)
    langs = args.lang.split(',')
    if csv.endswith('.csv'):
        main(song_df=df,
            save_dir=args.save_dir,
            langs=langs)
    else:
        print('Enter the valid wiki table format csv file with ".csv" format after --songs')