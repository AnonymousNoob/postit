import requests
# Get a specific note
def get_notes(id):
    url = 'http://localhost:8000/notes/' 
    params = {'id': id}
    r = requests.get(url, params=params)
    notes = r.json()
    return notes

# Get all notes
def get_notes_all():
    url = 'http://localhost:8000/notes/' 
    r = requests.get(url)
    notes = r.json()
    return notes    