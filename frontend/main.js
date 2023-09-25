async function getLyrics() {
    container = document.getElementById('container')
    container.innerHTML = ''
    const artist = document.getElementById('artistInput').value;
    const title = document.getElementById('titleInput').value;
    const headers = new Headers();
    headers.append('Artist', artist);
    headers.append('Title', title);
    const resp = await fetch('http://127.0.0.1:9999/lyrics', { method: 'GET', headers: headers });
    let respText = await resp.text();
    const blankPage = "AZLyrics - Song Lyrics from A to ZA"
    if (respText.includes(blankPage)) {
        const customMessage = 'No lyrics found. Try something else';
        container.innerHTML = customMessage;
        return { 'result': customMessage };
    }
    const respJson = JSON.parse(respText);
    container.innerHTML = respJson.result;
    return respJson;
}

async function getLyricsAndChords() {
    container = document.getElementById('container')
    container.innerHTML = ''
    const artist = document.getElementById('artistInput').value;
    const title = document.getElementById('titleInput').value;
    const headers = new Headers();
    headers.append('Artist', artist);
    headers.append('Title', title);
    try {
        const resp = await fetch('http://127.0.0.1:9999/chords', { method: 'GET', headers: headers });
        if (resp.ok) {
            const respText = await resp.json(); 
            container.innerHTML = respText.text;
            return respText;
        } else {
            const errorText = await resp.text();
            container.innerHTML = errorText;
            return errorText;
        }
    } catch (error) {
        console.error('Fetch error:', error);
    }
}