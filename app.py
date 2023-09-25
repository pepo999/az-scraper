import requests
from bs4 import BeautifulSoup

def scrape(artist, title):
    f_artist = artist.lower().replace(' ', '')
    f_title = title.lower().replace(' ', '')
    page = requests.get(f'https://www.azlyrics.com/lyrics/{f_artist}/{f_title}.html')
    soup = BeautifulSoup(page.content, 'html.parser')
    children = list(soup.children)
    container_text = children[-2].text
    text_to_remove = """Lyrics | AZLyrics.com




































A
B
C
D
E
F
G
H
I
J
K
L
M
N
O
P
Q
R
S
T
U
V
W
X
Y
Z
#








 Search













































"""
    alphabet_to_remove = """A
B
C
D
E
F
G
H
I
J
K
L
M
N
O
P
Q
R
S
T
U
V
W
X
Y
Z
# Search
"""
    blank_lines = """


"""
    filtered_text = container_text.replace(text_to_remove, '').replace(blank_lines, '').replace(alphabet_to_remove, '').split('Submit') 
    lyrics = filtered_text[0].split('"')  
    result = lyrics[-1] + """

""" 
    print(str(result))
    return str(result)

artist_input = str(input('Artista: '))
song_input = str(input('Canzone: '))


scrape(artist_input, song_input)