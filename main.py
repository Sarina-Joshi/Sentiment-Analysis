# We need to clean texts before any natural language processing
# Cleaning texts Steps
# 1) Create a text file and take text from it
# 2) Convert the letter into lowercase
# 3) Remove any punctuation

import string
from collections import Counter

import matplotlib.pyplot as plt
from nltk.corpus import stopwords
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize

text = open('read.txt', encoding='utf-8').read()
lower_case = text.lower()  # Converts to lower case
print(lower_case)
# print(string.punctuation)
cleaned_text = lower_case.translate(str.maketrans('', '', string.punctuation))  # Removes punctuations
print(cleaned_text)
tokenized_words = cleaned_text.split()  # Splits a string into a list
# print(tokenized_words)
stop_words = ["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself",
              "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself",
              "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that", "these",
              "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", "having", "do",
              "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", "while",
              "of", "at", "by", "for", "with", "about", "against", "between", "into", "through", "during", "before",
              "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under", "again",
              "further", "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", "both", "each",
              "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than",
              "too", "very", "s", "t", "can", "will", "just", "don", "should", "now"]
final_words = []
for word in tokenized_words:
    if word not in stop_words:
        final_words.append(word)
# print(final_words)

''' emotion_list=[]
with open('emotions.txt','r') as file:
    for line in file:
        clr_line = line.replace('\n','').replace(',','').replace("'",'').strip()
        word, emotion = clr_line.split(' : ')
        #print("Word:" + word + " " + "Emotion:" + emotion)
    	if word in final_words:
            emotion_list.append(emotion)
print(emotion_list) '''

emotion_list = []
with open('emotions.txt', 'r') as file:
    for line in file:
        clear_line = line.replace("\n", '').replace(",", '').replace("'", '').strip()
        word, emotion = clear_line.split(':')

        if word in final_words:
            emotion_list.append(emotion)

        # for words in final_words:
        #     if words in word:
        #         emotion_list.append(emotion)
    print(emotion_list)
w = Counter(emotion_list)
print(w)


def sentiment_analyse(sentiment_text):
    score = SentimentIntensityAnalyzer().polarity_scores(sentiment_text)
    if score['neg'] > score['pos']:
        print("Negative Sentiment")
    elif score['neg'] < score['pos']:
        print("Positive Sentiment")
    else:
        print("Neutral Sentiment")


sentiment_analyse(cleaned_text)

fig, axis = plt.subplots()
axis.bar(w.keys(), w.values())
fig.autofmt_xdate()
plt.savefig('graph.png')
plt.show()
