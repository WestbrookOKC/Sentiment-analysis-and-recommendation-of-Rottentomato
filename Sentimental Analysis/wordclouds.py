from wordcloud import WordCloud
import matplotlib.pyplot as plt

# Read the whole text.
text = open('/Users/fengkaiqi/Desktop/python/clean.txt').read()

# Generate a word cloud image
wordcloud = WordCloud().generate(text)
# Display the generated image:
# the matplotlib way:
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
#save the png
wordcloud.to_file('/Users/fengkaiqi/Desktop/python/wordsShow.png')
plt.show()