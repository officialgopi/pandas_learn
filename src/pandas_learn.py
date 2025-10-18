import pandas as pd


def use_pandas(data):
    # Print the first few rows
    print(data.head(10)) #initial 5 rows
    print(type(data)) # <class 'pandas.core.frame.DataFrame'>
    # Print the last  few rows
    print(data.tail(10)) # initial last 5 rows
    # access a column
    print(data['PassengerId'])


def main():
    try:
        # Load the Titanic dataset  
        data = pd.read_csv('./dataset/titanic.csv')
        use_pandas(data)
    except FileNotFoundError:
        print("The dataset file was not found. Please ensure the path is correct.")
    # print(data)



main()

