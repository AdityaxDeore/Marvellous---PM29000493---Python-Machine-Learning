"""
Question 3:
Split the dataset into training and testing sets using train_test_split. Use test_size = 0.3 and random_state = 42.
"""

import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split

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

def ShowSplit(XTrain, XTest, YTrain, YTest):
    print("X_train shape:", XTrain.shape)
    print("X_test shape:", XTest.shape)
    print("y_train shape:", YTrain.shape)
    print("y_test shape:", YTest.shape)

def main():
    print("----- Train Test Split : Ball Dataset -----")
    df = LoadData()
    EncodeFeatures(df)
    x_train, x_test, y_train, y_test = SplitData(df)
    ShowSplit(x_train, x_test, y_train, y_test)

if __name__ == "__main__":
    main()
