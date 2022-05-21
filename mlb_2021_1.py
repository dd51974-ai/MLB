import csv
data = dict()
with open("MLB_2021.csv", "r") as open_mlb_text:
    reader = csv.reader(open_mlb_text, delimiter="\t", doublequote=True, lineterminator="\r\n", quotechar='"',
                        skipinitialspace=True)
    header = next(reader)
    print(reader)