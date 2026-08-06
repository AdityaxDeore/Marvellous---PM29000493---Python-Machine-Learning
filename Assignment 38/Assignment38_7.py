"""
Question 7:
Predict the label for a new ball with Surface = Rough and Colour = Red.
"""

import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

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
    surface_le = LabelEncoder()
    colour_le = LabelEncoder()
    label_le = LabelEncoder()

    DataFrame['Surface'] = surface_le.fit_transform(DataFrame['Surface'])
    DataFrame['Colour'] = colour_le.fit_transform(DataFrame['Colour'])
    DataFrame['Label'] = label_le.fit_transform(DataFrame['Label'])

    return surface_le, colour_le, label_le

def SplitData(DataFrame):
    X = DataFrame[['Surface', 'Colour']]
    Y = DataFrame['Label']

    return train_test_split(X, Y, test_size=0.3, random_state=42)

def TrainModel(XTrain, YTrain):
    model = DecisionTreeClassifier(random_state=42)
    model.fit(XTrain, YTrain)

    return model

def PredictResult(Model, SurfaceEncoder, ColourEncoder, LabelEncoder):
    new_ball = [[SurfaceEncoder.transform(['Rough'])[0],
                 ColourEncoder.transform(['Red'])[0]]]
    prediction = Model.predict(new_ball)

    print("New ball: Surface = Rough, Colour = Red")
    print("Predicted Label:", LabelEncoder.inverse_transform(prediction)[0])

def main():
    print("----- Decision Tree : Ball Classification -----")
    df = LoadData()
    surface_le, colour_le, label_le = EncodeFeatures(df)
    x_train, x_test, y_train, y_test = SplitData(df)
    model = TrainModel(x_train, y_train)
    PredictResult(model, surface_le, colour_le, label_le)

if __name__ == "__main__":
    main()
