import re
import string

import numpy as np
import pandas as pd
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import f1_score
from sklearn.model_selection import KFold
from sklearn.naive_bayes import MultinomialNB, BernoulliNB

# # In case of any corpus are missing
# nltk.download()
df = pd.read_csv('./asg1_train.csv')
test = pd.read_csv('./asg1_test.csv')
stop_words = stopwords.words("english")


def text_preproc(x):
    x = x.lower()
    x = ' '.join([word for word in x.split(' ') if word not in stop_words])
    x = x.encode('ascii', 'ignore').decode()
    x = re.sub(r'https*\S+', ' ', x)
    x = re.sub(r'@\S+', ' ', x)
    x = re.sub(r'#\S+', ' ', x)
    x = re.sub(r'\'\w+', '', x)
    x = re.sub('[%s]' % re.escape(string.punctuation), ' ', x)
    x = re.sub(r'\w*\d+\w*', '', x)
    x = re.sub(r'\s{2,}', ' ', x)
    return x


df['clean_text'] = df.text.apply(text_preproc)
test['clean_text'] = test.text.apply(text_preproc)

vectorizer = TfidfVectorizer()
x = vectorizer.fit_transform(df['clean_text']).toarray()
df_new = pd.DataFrame(x, columns=vectorizer.get_feature_names_out())
X_test = vectorizer.transform(test['clean_text']).toarray()
test_new = pd.DataFrame(X_test, columns=vectorizer.get_feature_names_out())

x = df_new.values
y = df.text.values
kfold = KFold(n_splits=10)
# Define the model
nb_multinomial = MultinomialNB()
nb_bernoulli = BernoulliNB()


# As a storage of the model's performance
def calculate_f1(model):
    metrics = []

    for train_idx, test_idx in kfold.split(x):
        x_train, x_test = x[train_idx], x[test_idx]
        y_train, y_test = y[train_idx], y[test_idx]
        model.fit(x_train, y_train)
        y_pred = model.predict(x_test)
        metrics.append(f1_score(y_test, y_pred, average='weighted'))

    # Retrieve the mean of the result
    print("%.3f" % np.array(metrics).mean())


calculate_f1(nb_multinomial)
calculate_f1(nb_bernoulli)


def predict_to_csv(model, X, y):
    model.fit(X, y)
    X_test = test_new.values
    y_pred = model.predict(X_test)
    # Preparing submission
    submission = pd.DataFrame()
    submission['id'] = test['id']
    submission['target'] = y_pred
    submission.to_csv('file_name.csv', index=False)
    # Validate
    submission = pd.read_csv('file_name.csv')
    print(submission.head())


nb_bernoulli = BernoulliNB()
x = df_new.values
y = df.target.values
predict_to_csv(nb_bernoulli, x, y)
