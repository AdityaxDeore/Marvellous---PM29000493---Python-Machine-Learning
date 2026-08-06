"""
Question 2:
Convert categorical features (Surface, Colour) into numerical form using Label Encoding.
"""

import pandas as pd
from sklearn.preprocessing import LabelEncoder

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

def ShowEncoded(DataFrame, SurfaceEncoder, ColourEncoder, LabelEncoder):
    print("Surface classes:", list(SurfaceEncoder.classes_))
    print("Colour classes:", list(ColourEncoder.classes_))
    print("Label classes:", list(LabelEncoder.classes_))
    print()
    print(DataFrame)

def main():
    print("----- Label Encoding : Ball Dataset -----")
    df = LoadData()
    surface_le, colour_le, label_le = EncodeFeatures(df)
    ShowEncoded(df, surface_le, colour_le, label_le)

if __name__ == "__main__":
    main()
