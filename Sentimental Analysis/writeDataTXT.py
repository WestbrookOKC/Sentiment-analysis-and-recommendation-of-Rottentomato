import csv
#get the comment from review.csv
with open('/review.csv', 'r', encoding='unicode_escape') as csvfile:
    reader = csv.DictReader(csvfile)
    column = [row['comment'] for row in reader]
#put comment from csv to txt
with open("/SentimentalWords.txt", 'wt', encoding='UTF-8') as f:
    for i in (column):
        print(i, file=f)