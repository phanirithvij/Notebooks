
# coding: utf-8

# In[1]:


from anime_downloader import get_anime_class

# Both of the below functions return the same class
NineAnime = get_anime_class('9anime')


# In[2]:


anime = NineAnime('https://www4.9anime.is/watch/dragon-ball-super-dub.r65p', quality='720p')
	
print(anime.title)
print(anime.image)  # Poster. This will be renamed to poster in a future release.
print(len(anime))  # No of episodes for the anime
print(anime.url)  # The site url for the anime.
print(anime.quality)
print(anime.meta)  # A dictionary containing extra metadata. Can be empty and can vary across sites.
print(anime.sitename)  # In case you want to know which site.


# In[3]:


ep = anime[0]


# In[4]:


e_s = ep.__dict__

print(e_s)


# In[6]:


KissAnime = get_anime_class("http://kissanime.ru/Anime/Gintama-Shirogane-no-Tamashii-hen-2/Episode-354?id=147594&s=rapidvideo")

onepiece = KissAnime("http://kissanime.ru/Anime/One-Piece/Episode-844?id=147580")

print(onepiece)

