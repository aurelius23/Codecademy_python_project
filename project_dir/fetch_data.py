import requests
url = "http://www.songlyrics.com/iron-maiden/iron-maiden-lyrics/"
response = requests.get(url)
import bs4
soup = bs4.BeautifulSoup(response.text)
x = soup.find(id="songLyricsDiv")
file = x.get_text()
file = file.encode('ascii','ignore')
file = file.split("\n")
file = " ".join(file)
file = file.replace("!","")
file = file.replace("?","")
file = file.replace(",","")
text = open("lyric.txt", "w")
text.write(file)
text.close()
