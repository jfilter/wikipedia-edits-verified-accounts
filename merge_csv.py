import csv
from pathlib import Path

folder = 'recent_changes'

all_csv = [pth for pth in Path(folder).iterdir()
            if pth.suffix == '.csv']

header = None
rows = []

for f_csv in all_csv:
    with open(f_csv) as csvfile:
        reader = csv.reader(csvfile)
        header = next(reader) # read header
        rows += list(reader)

with open(f'{folder}_all.csv', 'w') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(header)
    writer.writerows(rows)
