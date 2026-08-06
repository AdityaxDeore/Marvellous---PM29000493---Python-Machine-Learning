"""
Question 9:
Display the trained Decision Tree structure using: from sklearn import tree, tree.plot_tree(model).
"""

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn import tree

def LoadData():
    data = {
        'Surface': ['Rough', 'Rough', 'Rough', 'Smooth', 'Smooth',
                    'Smooth', 'Rough', 'Rough', 'Smooth', 'Smooth'],
        'Colour':  ['Red', 'Red', 'White', 'White', 'White',
                    'Red', 'Red', 'White', 'White', 'Red'],
        'Label':   ['Tennis', 'Tennis', 'Tennis', 'Cricket', 'Cricket',
                    'Cricket', 'Tennis', 'Tennis', 'Cricket', 'Cricket']
    }

    return pd.DataFrame(data)

def EncodeFeatures(DataFrame):
    label_le = LabelEncoder()

    DataFrame['Surface'] = LabelEncoder().fit_transform(DataFrame['Surface'])
    DataFrame['Colour'] = LabelEncoder().fit_transform(DataFrame['Colour'])
    DataFrame['Label'] = label_le.fit_transform(DataFrame['Label'])

    return label_le

def SplitData(DataFrame):
    X = DataFrame[['Surface', 'Colour']]
    Y = DataFrame['Label']

    return train_test_split(X, Y, test_size=0.3, random_state=42)

def TrainModel(XTrain, YTrain):
    model = DecisionTreeClassifier(random_state=42)
    model.fit(XTrain, YTrain)

    return model

def ShowTree(Model, LabelEncoder):
    plt.figure(figsize=(10, 6))
    tree.plot_tree(Model,
                   feature_names=['Surface', 'Colour'],
                   class_names=list(LabelEncoder.classes_),
                   filled=True, rounded=True)
    plt.title("Decision Tree - Ball Classification")
    plt.savefig("decision_tree.png")
    print("Decision tree saved as decision_tree.png")

def main():
    print("----- Decision Tree : Ball Classification -----")
    df = LoadData()
    label_le = EncodeFeatures(df)
    x_train, x_test, y_train, y_test = SplitData(df)
    model = TrainModel(x_train, y_train)
    ShowTree(model, label_le)

if __name__ == "__main__":
    main()
