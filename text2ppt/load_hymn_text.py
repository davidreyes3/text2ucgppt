import csv

# CSV file needs to formatted with
# - hymn number
# - one line of text for each slide => if there should be 4 lines for the first verse in hymnal, there should be 4 lines of text in CSV file

HYMN_TEXT_PATH = '../resources/hymn_text.csv'


def load_hymn_text():
    with open(HYMN_TEXT_PATH, mode='r', newline='') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=':')
        data = list(csv_reader)

    for row in data[1:]:
        print(row)

    return data[1:]

load_hymn_text()