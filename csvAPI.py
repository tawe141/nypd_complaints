import csv


# Returns [header, data]
def getData():
  with open('data/allegations_20200726939.csv') as f:
    reader = csv.reader(f)
    rows = [row for row in reader]
  return rows[0], rows[1:]
