from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

def do(t):
    if t=="get-1k":
        df = pd.read_csv("../dummy/fake-news/train.csv")
        df = df[1:1001]
        df.to_csv("train-1k.csv")
    elif t=="nb-train":
        df = pd.read_csv("train-1k.csv")
        df = df[1:100]
        print(df.head(10))
        df["lentext"] = df["text"].map(len)
        df.describe()

        print(df["lentext"])

        model = GaussianNB()

        x_train, x_test, y_train, y_test = train_test_split(
            df["lentext"], 
            df["label"], 
            test_size = 0.2, 
            random_state = 5
        )

        x_train = np.array(x_train).reshape(-1, 1)
        x_test = np.array(x_test).reshape(-1, 1)

        nbTrain = model.fit(x_train, y_train)
        y_pred = nbTrain.predict(x_test)
        np.array(y_pred)
        np.array(y_test)

        nbTrain.predict_proba(x_test)
        confusion_matrix(y_test,y_pred)
        print(classification_report(y_test, y_pred))
    elif t=="1":
        print("1")

# do("get-1k")
do("nb-train")