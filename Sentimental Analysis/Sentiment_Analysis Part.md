Sentiment Analysis Part

Kaiqi Feng

情感分析需要得到用户对某个电影评论的数据，之后对得到的数据进行数据预处理。例如，分词，删去停用词，词干提取以及词形复原。接下来，进行模型处理，选取适合的模式。最后，输出模型处理后的结果，让预测结果可视化。

我们这里的情感分析采用了一个方便快捷的方法：Huggingface-pipepline。它具备了数据预处理、模型处理、模型输出后处理等步骤，可以直接输入原始数据，然后给出预测结果，十分方便。大家可以理解其为一个端对端的工具。

因为我们面向的对象是一个来自多语言的电影评论，因此我们在选择模型的时候需要谨慎一点。pipeline的默认模型只可以分析英文的语言，而不能对法语俄语等语言进行处理。sentimentanalyzer = pipeline('sentiment-analysis', model="nlptown/bert-base-multilingual-uncased-sentiment")。
结果会有积极或者消极两个label以及它们的倾向性比例，遍历保持在excel表中。

重词云：在这里，采用jieba分词方法和清华大学提供的分词表对评论进行分析，对出现频率较高的单词使用matplotlib将其可视化，之后保存为png文件。

Sentiment analysis needs to obtain the data of the user's comments on a certain movie, and then perform data preprocessing on the obtained data. For example, word segmentation, deletion of stop words, stemming and lemmatisation. Next, perform model processing and select a suitable model. Finally, output the processed results of the model to visualize the predicted results.

Our sentiment analysis here uses a convenient and quick method: Huggingface-pipepline. It has the steps of data preprocessing, model processing, and model output post-processing. It can directly input the original data and then give the prediction results, which is very convenient. You can understand it as an end-to-end tool.

Because our target is a movie review from multiple languages, we need to be careful when choosing a model. The pipeline's default model can only analyze English languages, but cannot process languages ​​such as French and Russian. Eg. sentimentanalyzer = pipeline('sentiment-analysis', model="nlptown/bert-base-multilingual-uncased-sentiment").
As a result, there will be two labels, positive or negative, and their preference ratios, and the results will be stored in the excel sheet.

WordCloud: Here, the jieba word segmentation method and the word segmentation table provided by TsingHua University are used to analyze the comments, and the words that appear frequently are visualized using matplotlib, and then saved as png files.
