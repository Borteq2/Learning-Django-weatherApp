# Training-weatherApp

---

This project uses `poetry` instead of `pip`. 
If you want to use only pip - project uses pure `Django` and `Requests` libs.

---
#### For launch my way:
- make sure you already have `poetry` on yout PC. If not - `pip install poetry` will add it to you, or use any another way to get poetry
- clone project
- at start dir (`Training-weatherApp`) launch in terminal: `poetry init`. Maybe it says thai .toml already there, it means this spet already done by me for you. :)
- `poetry install` (it may lag sometime, dont worry just wait)
- to make sure all ok, launch `poetry show --tree`. Must return beautiful tree view for dependencies (with short descriptions, wow!)
- `cd WeatherApp`
- `poetry shell` - it will drop you in default Python mode for terminal, pretty good
- `python manage.py runserver` (for Windows ofc, python3 if you have red eyes)
- click to link in terminal, it will route you into localhost
- use it with pleasure and wow-effect

---
- For adding new city to dashboard just add your city name in input with corresponding placeholder. Pretty easy, huh?
- Yeah, at born-time this app dont have a deletint mechanism because im lazy. Later will do. 
- For now you can add `/admin` to app url (in browser ofc) and enter admin panel with superuser credentials.
- Where you can get it? Use `python manage.py creatusuperuser` at terminal and follow instructions. Wow, such coding moment
