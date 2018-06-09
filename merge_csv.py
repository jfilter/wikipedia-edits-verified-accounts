import os
import csv
import sys

# merging the individual csv to one huge csv
# TODO: should use ordinary csv reader/writer instead of dict reader/writer

path = 'data/allrevisions'
files = os.listdir(path)

csv.field_size_limit(sys.maxsize)

fieldnames = ['page_id', 'page_title', 'revid', 'parentid', 'user', 'timestamp',
              'comment', 'parsedcomment', 'contentformat', 'contentmodel', 'size', 'tags', 'bot', 'new', 'minor', 'data', 'texthidden', 'suppressed', 'commenthidden']

data = []

for f in files[:10]:
    with open(f'{path}/{f}', 'r', newline='') as csvfile:

        reader = csv.DictReader(csvfile, fieldnames=fieldnames)
        data += list(reader)
        print(len(data))

with open('data/allrevisions_all.csv', 'w', newline='') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(data)
    print('wrote file')
