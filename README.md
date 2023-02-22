# Training-weatherApp

---

This project uses `poetry` instead of `pip`. 
If you want to use only pip - project uses pure `Django` and `Requests` libs.

---
#### For launch my way:
- make sure you already have `poetry` on yout PC. If not - `pip install poetry` will add it to you, or use any another way to get poetry
- clone project
- at start dir (`Training-weatherApp`) launch in terminal: `poetry init`. Maybe it says something like .toml already there, it means this step already done by me for you. :)
- `poetry install` (it may lag sometimes, dont worry, just wait)
- to make sure all ok, launch `poetry show --tree`. Must return beautiful tree view for dependencies (with short descriptions, wow!)
```
django 4.1.7 A high-level Python web framework that encourages rapid development and clean, pragmatic design.
├── asgiref >=3.5.2,<4
├── sqlparse >=0.2.2
└── tzdata *
requests 2.28.2 Python HTTP for Humans.
├── certifi >=2017.4.17
├── charset-normalizer >=2,<4
├── idna >=2.5,<4
└── urllib3 >=1.21.1,<1.27
```
- `cd WeatherApp`
- `poetry shell` - it will drop you in default Python mode for terminal, pretty good
- `python manage.py runserver` (for Windows ofc, python3 if you have red eyes)
- click to link in terminal, it will route you into localhost
- use it with pleasure and wow-effect

---
- For adding new city to dashboard just add your city name in input with corresponding placeholder. Pretty easy, huh?
- Yeah, at born-time this app dont have a deleting mechanism because im lazy. Later will do. 
- For now you can add `/admin` to app url (in browser ofc) and enter admin panel with superuser credentials.
- Where you can get it? Use `python manage.py creatusuperuser` at terminal and follow instructions. Wow, such coding moment
- For what you want admin panel? For manyally add and delete cities from db and dashboard. Not wow, not cool
