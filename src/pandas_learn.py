import pandas as pd


def use_pandas(data):
    # Print the first few rows
    print(data.head(10)) #initial 5 rows
    print(type(data)) # <class 'pandas.core.frame.DataFrame'>
    # Print the last  few rows
    print(data.tail(10)) # initial last 5 rows
    # access a column
    print(data['PassengerId'])
    # Series is a one-dimensional array-like structure in Pandas that can hold a sequence of value of any data type. Each value in a Series is associated with an index label, which allows for easy access and manipulation of the data.Custom index labels can be assigned to a Series during its creation or modified later.
    print(type(data['PassengerId'])) # <class 'pandas.core.series.Series'>

    #create a series
    series_scalar = pd.Series(10,index = ['a','b','c' ,'d','e','f','g','h','i','j'])
    print(series_scalar)


def main():
    try:
        # Load the Titanic dataset  
        data = pd.read_csv('./dataset/titanic.csv')
        use_pandas(data)
    except FileNotFoundError:
        print("The dataset file was not found. Please ensure the path is correct.")
    # print(data)



main()

