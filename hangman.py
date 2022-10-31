import uuid, string, random
from words import wordlist


sessions = {}

def generate_gamestate(word, guesses):
    output = ""
    for character in word:
        if character in guesses:
            output += character
        else:
            output+= ("-")
    return (output)

def format_output(session):
    session = dict(session)
    session.pop('word')
    return session


def newSession():
    localID = str(uuid.uuid4())
    word = random.choice(list(wordlist.keys()))
    definition = wordlist[word]
    correctguesses = []
    incorrectguesses = []
    gamestate = generate_gamestate(word, correctguesses)

    bodyparts = 0
    session = { 'context': localID, 'word': word, 'definition': definition, 'gamestate': gamestate, 'correctguesses': correctguesses, 
                'incorrectguesses': incorrectguesses, 'bodyparts': bodyparts}

    sessions[localID] = session
    return(format_output(session))

def keypress(context, key):
    session = sessions.get(context)
    key = key.lower()
    if (session == None):
        return {"status": 'ERR', "reason": "Invalid Session"}
    print("Session = " + str(session))
    print("Key = " + key)
    if ((len(key) != 1) or (key not in string.ascii_lowercase)):
        return {"status": 'ERR', "reason": "Invalid Key (single lowercase character only"}
    if ((key in session['correctguesses']) or (key in session['incorrectguesses'])):
        return {"status": 'ERR', "reason": "Letter already guessed"}

    if key in session['word']:
        # Letter correctly guessed
        session['correctguesses'].append(key)
        session['gamestate'] = generate_gamestate(session['word'], session['correctguesses'])
    else:
        session['bodyparts'] += 1
        session['incorrectguesses'].append(key)
    print("Session = " + str(session))
    return(format_output(session))
