import csv
import pathlib

import requests

# create folders for later use
pathlib.Path('data/recent_changes').mkdir(parents=True, exist_ok=True) 
pathlib.Path('data/allrevisions').mkdir(parents=True, exist_ok=True) 

base_url = 'https://de.wikipedia.org/w/api.php?action=query&format=json&list=categorymembers&cmtitle=Kategorie%3ABenutzer%3AVerifiziert&cmlimit=500'
cont = ''

user = []

while True:
    url = base_url + '&cmcontinue=' + cont
    r = requests.get(url)
    print(r.status_code)
    r.raise_for_status()

    r_json = r.json()

    if "query" in r_json:
        for item in r_json["query"]["categorymembers"]:
            title = item['title']
            index_sep = title.index(':')  # cut away 'Benutzer(in):'
            title = title[index_sep + 1:]
            title = title.replace(' ', '_')  # spaces need to be converted
            user.append({'name': title})

    if "continue" not in r_json:
        print(r_json)
        break
    else:
        cont = r_json["continue"]["cmcontinue"]


with open('data/users.csv', 'w', newline='') as csvfile:
    fieldnames = ['name']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerows(user)
