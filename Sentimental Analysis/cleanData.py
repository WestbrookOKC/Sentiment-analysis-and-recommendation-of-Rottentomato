#wordClouds
#coding=utf-8
import imageio
import matplotlib.pyplot as plt
#from scipy.misc import imread
from imageio import imread
from nltk import word_tokenize
from nltk.corpus import stopwords
from wordcloud import WordCloud
import jieba, codecs
from collections import Counter
#sjy sentimental analysis
import numpy as np
from snownlp import SnowNLP
import matplotlib.pyplot as plt
import imageio
import jieba, codecs

from collections import Counter

text = codecs.open('SentimentalWords.txt', 'r', encoding='utf-8').read()

text_jieba = jieba.cut(text)


#Remove StopWords

# create stopwords list from HaGongDa stopwords.txt

def stopwordslist():

    stopwords = [line.strip() for line in open('stopwords.txt',encoding='UTF-8').readlines()]

    return stopwords

# segment sentence
def seg_depart(sentence):
    # seg txt
    sentence_depart = jieba.cut(sentence.strip())
    # get stopwords list
    stopwords = stopwordslist()
    outstr = ''
    # remove stop word
    for word in sentence_depart:

        if word not in stopwords:

            if word != '\t':

                outstr += word

                outstr += " "
    return outstr

# set file path
filename = "SentimentalWords.txt"

outfilename = "clean.txt"

inputs = open(filename, 'r', encoding='UTF-8')

outputs = open(outfilename, 'w', encoding='UTF-8')

# write answer in ou.txt

for line in inputs:

    line_seg = seg_depart(line)

    outputs.write(line_seg + '\n')

outputs.close()

inputs.close()

print("删除停用词和分词成功！！！")





