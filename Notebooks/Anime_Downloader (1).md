

```python
from anime_downloader import get_anime_class

# Both of the below functions return the same class
NineAnime = get_anime_class('9anime')
```


```python
anime = NineAnime('https://www4.9anime.is/watch/dragon-ball-super-dub.r65p', quality='720p')
	
print(anime.title)
print(anime.image)  # Poster. This will be renamed to poster in a future release.
print(len(anime))  # No of episodes for the anime
print(anime.url)  # The site url for the anime.
print(anime.quality)
print(anime.meta)  # A dictionary containing extra metadata. Can be empty and can vary across sites.
print(anime.sitename)  # In case you want to know which site.

```

    Dragon Ball Super (Dub)
    http://static.akacdn.ru/static/images/2018/04/5d8245338b23afea9ca957c5f7d44f98.jpg
    70
    https://www4.9anime.is/watch/dragon-ball-super-dub.r65p
    720p
    {'Genre': 'Action, Adventure, Comedy, Fantasy, Martial Arts, Shounen, Super Power', 'Studios': 'Toei Animation', 'Status': 'Airing', 'Premiered': 'Summer 2015', 'Rating': '8.5 / 1,175 times', 'Scores': '7.5 / 89,002', 'Type': 'TV Series', 'Duration': '23 min/ep', 'Views': '1,908,663', 'Quality': 'HD', 'Date aired': 'Jul 05, 2015 to ?'}
    9anime



```python
ep = anime[0]
```


```python
e_s = ep.__dict__

print(e_s)
```

    {'_sources': [<anime_downloader.extractors.rapidvideo.RapidVideo object at 0x7f0b48542f60>], 'url': 'n0k66l', 'ep_no': 1, 'quality': '720p', 'pretty_title': 'Dragon Ball Super (Dub)-1', '_parent': 
    Site: 9anime
    Anime: Dragon Ball Super (Dub)
    Episode count: 70
    }



```python
KissAnime = get_anime_class("http://kissanime.ru/Anime/Gintama-Shirogane-no-Tamashii-hen-2/Episode-354?id=147594&s=rapidvideo")

onepiece = KissAnime("http://kissanime.ru/Anime/One-Piece/Episode-844?id=147580")

print(onepiece)

```


    ---------------------------------------------------------------------------

    AttributeError                            Traceback (most recent call last)

    <ipython-input-6-a7526f558fdb> in <module>()
          1 KissAnime = get_anime_class("http://kissanime.ru/Anime/Gintama-Shirogane-no-Tamashii-hen-2/Episode-354?id=147594&s=rapidvideo")
          2 
    ----> 3 onepiece = KissAnime("http://kissanime.ru/Anime/One-Piece/Episode-844?id=147580")
          4 
          5 print(onepiece)


    /usr/local/lib/python3.5/dist-packages/anime_downloader/sites/anime.py in __init__(self, url, quality, _skip_online_data)
         36         if not _skip_online_data:
         37             logging.info('Extracting episode info from page')
    ---> 38             self.get_data()
         39 
         40     @classmethod


    /usr/local/lib/python3.5/dist-packages/anime_downloader/sites/baseanimecf.py in get_data(self)
         18         soup = BeautifulSoup(r.text, 'html.parser')
         19 
    ---> 20         self._scrape_metadata(soup)
         21 
         22         self._episode_urls = self._scarpe_episodes(soup)


    /usr/local/lib/python3.5/dist-packages/anime_downloader/sites/kissanime.py in _scrape_metadata(self, soup)
         98     def _scrape_metadata(self, soup):
         99         info_div = soup.find('div', {'class': 'barContent'})
    --> 100         self.title = info_div.find('a', {'class': 'bigChar'}).text
    

    AttributeError: 'NoneType' object has no attribute 'text'

