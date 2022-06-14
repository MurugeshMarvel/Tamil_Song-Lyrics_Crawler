from bs4 import BeautifulSoup
import requests
import webbrowser 
import pandas as pd

url = 'https://www.tamil2lyrics.com/s-p-balasubrahmanyam-songs/'

try:
    page = requests.get(url)
    page.raise_for_status()
    soup = BeautifulSoup(page.text, 'html.parser')
    song = soup.find('tbody', class_='row-hover').find_all('tr')
    y = []
    m = []
    s = []
    for i in song:
        year = i.find('td', class_='column-1').text
        movie = i.find('td', class_='column-2').a.text
        song = i.find('td', class_='column-3').a.text
        y.append(year)
        m.append(movie)
        s.append(song)
    dic = {'Year':y,
            'Movie': m,
            'Song':s}
    df = pd.DataFrame(dic)
    df.to_csv('spb_tamil_songs.csv')

except Exception as e:
    print(e)
