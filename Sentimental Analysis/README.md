# Sematimental Analysis


## Getting Started

Start by exporting data from csv with label'comment'. We should get comment data from review.csv.

```
with open('/Users/fengkaiqi/Desktop/python/review.csv','r',encoding='unicode_escape') as csvfile:
    reader = csv.DictReader(csvfile)
    column = [row['comment'] for row in reader]
```

Then we should install transformers, after that download some neccessary Tokenization.


```
pip3 install transformers
from transformers import pipeline
```

## Structure of Files


```
E:.
│   chromedriver
    clean.txt
    cleanData.py
    comment.txt
    SentimentalWords.txt
    sentimentAnalysis.py
    stopwords.txt
    wordclouds.py
    writeDataTXT.py
│
├─data
│       answer.csv
        info.csv
        review.csv
        wordsShow.png
```

## The functions of python files
cleanData.py: import stopwords list created by HaGongDa University, seperate Sentimental words and remove stopwords.

writeDataTXT.py: many data stored in csv, but it is better to use in txt style, so I transform it.

sentimentAnalysis.py: By using transformer pipeline, we do sentiment analysis to film comment

wordCloud.py: It is used to show the frequently used words in film comment.
