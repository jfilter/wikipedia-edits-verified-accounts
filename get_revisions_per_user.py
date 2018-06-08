import csv
import time

import requests


# if the script got disrupted and you want to continue with one specific user
# enter the user name here
continue_with_user = None


base_url = 'https://de.wikipedia.org/w/api.php?action=query&format=json&list=allrevisions&arvprop=ids%7Cflags%7Ctimestamp%7Cuser%7Csize%7Ccontentmodel%7Ccontent%7Ccomment%7Cparsedcomment%7Ctags&arvlimit=500'
cont = ''

users = []

with open('data/users.csv', newline='') as csvfile:
    reader = csv.reader(csvfile)
    next(reader)  # skip header
    for row in reader:
        users.append(row[0])

if continue_with_user is None:
    skip = False
else:
    skip = True

for user in users:
    if skip and user == continue_with_user:
        skip = False

    if skip:
        continue

    print(user)
    user_base_url = base_url + '&arvuser=' + user
    all_rev = []
    cont = None

    while True:
        print(len(all_rev))
        url = user_base_url
        if cont:
            url += '&arvcontinue=' + cont
        print(url)

        num_fails = 0
        r = None
        while num_fails < 5:
            r = requests.get(url)
            print(r.status_code)
            if r.ok:
                break
            num_fails += 1
            time.sleep(1)
        r.raise_for_status()
        r_json = r.json()

        if "query" in r_json:
            for page in r_json["query"]["allrevisions"]:
                page_id = page['pageid']
                page_title = page['title']

                for rev in page['revisions']:
                    rev['page_id'] = page_id
                    rev['page_title'] = page_title
                    if '*' in rev:
                        rev['data'] = rev.pop('*')
                    all_rev.append(rev)

        if "continue" not in r_json:
            print(r_json)
            break
        else:
            cont = r_json["continue"]["arvcontinue"]

    with open(f'data/allrevisions/{user}.csv', 'w', newline='') as csvfile:
        fieldnames = ['page_id', 'page_title', 'revid', 'parentid', 'user', 'timestamp',
                      'comment', 'parsedcomment', 'contentformat', 'contentmodel', 'size', 'tags', 'bot', 'new', 'minor', 'data', 'texthidden', 'suppressed', 'commenthidden']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(all_rev)
        print('wrote file')
