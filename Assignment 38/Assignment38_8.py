"""
Question 8:
Calculate accuracy of the model using accuracy_score.
"""

import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

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
    DataFrame['Surface'] = LabelEncoder().fit_transform(DataFrame['Surface'])
    DataFrame['Colour'] = LabelEncoder().fit_transform(DataFrame['Colour'])
    DataFrame['Label'] = LabelEncoder().fit_transform(DataFrame['Label'])

def SplitData(DataFrame):
    X = DataFrame[['Surface', 'Colour']]
    Y = DataFrame['Label']

    return train_test_split(X, Y, test_size=0.3, random_state=42)

def TrainModel(XTrain, YTrain):
    model = DecisionTreeClassifier(random_state=42)
    model.fit(XTrain, YTrain)

    return model

def CalculateAccuracy(Model, XTest, YTest):
    y_pred = Model.predict(XTest)
    accuracy = accuracy_score(YTest, y_pred)

    print("Actual values:   ", list(YTest))
    print("Predicted values:", list(y_pred))
    print("Accuracy:", accuracy)

def main():
    print("----- Decision Tree : Ball Classification -----")
    df = LoadData()
    EncodeFeatures(df)
    x_train, x_test, y_train, y_test = SplitData(df)
    model = TrainModel(x_train, y_train)
    CalculateAccuracy(model, x_test, y_test)

if __name__ == "__main__":
    main()
