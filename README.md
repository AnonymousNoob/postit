# Post-It
## Pre-Requisites

```
#install the dependencies
pip install -r requirements.txt
```

## Usage

> Bash
```
export DJANGO_SETTINGS_MODULE=postit.local_settings
```
> Windows Shell
```
set DJANGO_SETTINGS_MODULE=postit.local_settings
```

```
python manage.py makemigrations notes
python manage.py migrate
```


## Features
- Versioning of changes made to individual notes.
- Autosave.
- Dynamic updations with AJAX.
- Edit any version of notes made.
- Add and Remove notes on the fly.
