import os
import requests
import bs4
from googlesearch import search

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

        for lang in self.langs:
            lang = 'English' if lang.lower().startswith('en') else 'Tamil'
            soup_finder = soup.find_all(class_ = 'tabcontent', id=lang.lower().title())
            tag = soup_finder[0]
            content_tags = ""
            for i in tag.children:
                if 'span style' not in str(i) and type(i) != bs4.element.NavigableString:
                    content_tags += (i.get_text())
                    content_tags += '\n\n'
            save_file_name = os.path.join(self.save_dir, f'{song_name}_{lang}.txt')
            with open(save_file_name, 'w') as f:
                f.write(content_tags)
        return None

    def get_lyrics(self,
                   song_names:list
                   ):
        for song in song_names:
            song_url = self._search_lyrics(song)
            self._parse_page(song_name=song, web_url=song_url)

