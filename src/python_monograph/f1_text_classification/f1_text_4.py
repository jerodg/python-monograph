# from sklearn.datasets import fetch_20newsgroups

# newsgroups_train = fetch_20newsgroups(subset="train", remove=("headers", "footers", "quotes"))
# newsgroups_test = fetch_20newsgroups(subset="test", remove=("headers", "footers", "quotes"))
import pandas as pd

train_data = pd.read_csv('./asg1_train.csv')
vectorizer = CountVectorizer()
x_train = vectorizer.fit_transform(train_data['text'])
y_train = train_data['label_text']

X_train = newsgroups_train.data
y_train = newsgroups_train.target
X_test = newsgroups_test.data
y_test = newsgroups_test.target
