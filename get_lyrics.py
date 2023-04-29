import os
import traceback
import requests
import bs4
from googlesearch import search
import traceback

class GetLyrics(object):
    def __init__(self,
                 save_dir:str,
                 langs:list = ['en', 'ta'],
                 src:str = 'tamil2lyrics.com'
                 ):
        self.save_dir = save_dir
        self.src = src
        self.langs = langs

    def _search_lyrics(self,
                     song_name:str
                     ) -> str:
        search_text = f"{song_name} tamil song lyric - {self.src}"
        web_url = search(search_text)[0]
        return web_url

    def _parse_page(self,song_name:str,
                   web_url:str
                   ):
        response = requests.get(web_url)
        soup = bs4.BeautifulSoup(response.text, "lxml")
        song_name = song_name.replace(" ", "_")
        for lang in self.langs:
            lang = 'English' if lang.lower().startswith('en') else 'Tamil'
            if not os.path.isfile(f'{self.save_dir}\{song_name}_{lang}.txt'):
                soup_finder = soup.find_all(class_ = 'tabcontent', id=lang.lower().title())
                tag = soup_finder[0]
                content_tags = ""
                for i in tag.children:
                    if 'span style' not in str(i) and type(i) != bs4.element.NavigableString:
                        content_tags += (i.get_text())
                        content_tags += '\n\n'
                save_file_name = os.path.join(self.save_dir, f'{song_name}_{lang}.txt')
                with open(save_file_name, 'w', encoding="utf-8") as f:
                    f.write(content_tags)
                print(f"## Downloaded Song Lyric - {song_name}_{lang}")
            else:
                print(f"## Already Downloaded Song Lyric - {song_name}_{lang}")
        return None

    def get_lyrics(self,
                   song
                   ):
        try:
            song_url = self._search_lyrics(song)
            self._parse_page(song_name=song, web_url=song_url)
        except Exception as exp:
            print(f"EXP - {exp}, \n {traceback.format_exc()}")

