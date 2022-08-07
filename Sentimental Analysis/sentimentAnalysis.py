# pip install transformers
import torch
from tqdm.auto import tqdm
from transformers import pipeline
import csv
# Allocate a pipeline for sentiment-analysis
from transformers.data import datasets
from transformers.pipelines.base import KeyDataset
import csv
#get the comment from review.csv
with open('/Users/fengkaiqi/Desktop/python/review.csv','r',encoding='unicode_escape') as csvfile:
    reader = csv.DictReader(csvfile)
    column = [row['comment'] for row in reader]
#print (column)

sentimentanalyzer = pipeline('sentiment-analysis')
#use sentimentanalyzer to do sentimental analysis
with open('answer.csv','a',encoding='utf-8',newline="") as csvfile:
    writer=csv.writer(csvfile)
    writer.writerow(["Label","Score"])
for col in column:
    if len(col) >=512:
        with open('answer.csv', 'a', encoding='utf-8', newline="") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow('FALSE')
        continue
    print( sentimentanalyzer(col))
    with open('answer.csv', 'a', encoding='utf-8', newline="") as csvfile:
        writer = csv.writer(csvfile)
        row = list(sentimentanalyzer(col))
        # r = dict(row)
        # print(r)
        # answer = r.values()
        # print(answer)
        # print(row[0])
        # r = row.values()
        writer.writerow(row)
    # csvfile.close()
#It return like [{'','','',''}]
#print(sentimentanalyzer('zhangyuqing is pig, always and forever a pig'))
#[{'label': 'POSITIVE', 'score': 0.9978193640708923}]



# Allocate a pipeline for question-answering
#question_answerer = pipeline('question-answering')
#print(question_answerer({'question': 'What is the name of the repository ?',
                  #       'context': 'Pipeline have been included in the huggingface/transformers repository'}))
#{'score': 0.5135612454720828, 'start': 35, 'end': 59, 'answer': 'huggingface/transformers'}



