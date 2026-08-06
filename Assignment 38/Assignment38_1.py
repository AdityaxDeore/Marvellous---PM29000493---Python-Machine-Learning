"""
Question 1:
Load a small sample dataset (create manually) with features and labels. Example data: Ball: Surface = Rough / Colour = Red / Label = Tennis; Surface = Smooth / Colour = White / Label = Cricket. Use pandas DataFrame to store this data.
"""

import pandas as pd

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

def ShowData(DataFrame):
    print(DataFrame)
    print()
    print("Shape:", DataFrame.shape)
    print("Columns:", list(DataFrame.columns))

def main():
    print("----- Ball Dataset -----")
    df = LoadData()
    ShowData(df)

if __name__ == "__main__":
    main()
