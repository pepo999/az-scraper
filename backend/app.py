from flask import Flask, jsonify, request
from flask_cors import CORS
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)
CORS(app)

@app.route("/lyrics")
def lyrics():
    artist = request.headers.get('Artist', '')
    title = request.headers.get('Title', '')
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
    return jsonify({"result": filtered_text[0]})

@app.route('/chords')
def chords():
    artist = request.headers.get('Artist', '')
    title = request.headers.get('Title', '')
    f_artist = artist.lower().replace(' ', '-')
    f_title = title.lower().replace(' ', '-')
    try:
        page = requests.get(f'https://www.e-chords.com/chords/{f_artist}/{f_title}')    
        soup = BeautifulSoup(page.content, 'html.parser')
        textarea = soup.find('pre')
        if textarea is None:
            return jsonify({"text": 'No chords found. Try something else'})
        textarea_content = textarea.text
        return jsonify({"text": textarea_content})
    except requests.exceptions.HTTPError as http_error:
        return jsonify({"error": f"HTTP Error: {http_error}"})
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    print('app running on port 9999')
    app.run("localhost", 9999)