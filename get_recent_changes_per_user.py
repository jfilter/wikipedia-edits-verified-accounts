import csv

import requests


base_url = 'https://de.wikipedia.org/w/api.php?action=query&format=json&list=recentchanges&rcprop=title%7Cids%7Csizes%7Cflags%7Cuse%7Ccomment%7Cuser%7Cparsedcomment%7Ctimestamp&rclimit=500&rctype=edit%7Cnew%7Clog%7Ccategorize'
cont = ''

users = []

with open('data/users.csv', newline='') as csvfile:
    reader = csv.reader(csvfile)
    next(reader)  # skip header
    for row in reader:
        users.append(row[0])

for user in users:
    print(user)
    user_base_url = base_url + '&rcuser=' + user
    recent_changes = []
    cont = None

    while True:
        url = user_base_url
        if cont:
            url += '&rccontinue=' + cont
        print(url)
        r = requests.get(url)
        print(r.status_code)
        print(len(recent_changes))
        r.raise_for_status()

        r_json = r.json()

        if "query" in r_json:
            recent_changes += r_json["query"]["recentchanges"]

        if "continue" not in r_json:
            print(r_json)
            break
        else:
            cont = r_json["continue"]["rccontinue"]

    with open(f'data/recent_changes/{user}.csv', 'w', newline='') as csvfile:
        fieldnames = ['type', 'ns', 'title', 'pageid', 'revid', 'old_revid', 'rcid',
                      'user', 'oldlen', 'newlen', 'timestamp', 'comment', 'parsedcomment', 'minor', 'new', 'bot']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(recent_changes)
        print('wrote file')
