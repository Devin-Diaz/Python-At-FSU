'''
In this assignment, you'll use a diamonds dataset to perform some data analysis tasks (please refer to
“Intro to Data Science: Working with CSV Files” pages and related source code under the Lecture Slides
module for related examples). 

This dataset is attached to this assignment and is also available as
diamonds.csv from various sources (e.g. Kaggle [https://www.kaggle.com/datasets] and Rdatasets
[https://vincentarelbundock.github.io/Rdatasets/datasets.html]). The dataset contains information on
53,940 diamonds, including each diamond's carats, cut, color, clarity, depth, table (flat top surface),
price and x, y and z measurements.

Write a program to perform the following tasks to study and analyze the diamonds dataset:
    1) Load the dataset into a pandas DataFrame. Use the following statement, which uses the first column
       of each record as the row index: df = pd.read_csv('diamonds.csv', index_col=0)

    2) Display the first seven rows of the DataFrame

    3) Display the last seven rows of the DataFrame

    4) Calculate and display the descriptive statistics for the numerical columns—carat, depth, table, price,
       x, y and z (Use the DataFrame method describe (which looks only at the numerical columns))

    5) Calculate and display the descriptive statistics for the categorical data (text) columns—cut, color and
       clarity (Use Series method describe)

    6) Display the unique category values (use the Series method unique)

    7) Display histograms of each numerical data column (call your DataFrame's hist method).
'''

# needed imports for reading and visualizing comma seperated value data
import pandas as pd
import matplotlib.pyplot as plt

# file path and converting csv file to dataframe
DIAMOND_CSV_FILE = "diamonds-1.csv"
df = pd.read_csv(DIAMOND_CSV_FILE, index_col=0)

# reading and parsing needed data
first_seven_rows = df.head(7)
last_seven_rows = df.tail(7)
numerical_cols = df.select_dtypes(include=['number'])
categorical_cols = (df.select_dtypes(include=object))
numerical_cols.hist(bins=30, figsize=(15, 8))

# utilizing data above for simple user use
def csv_exercise():
    while True:
        print('''
            DATA OPTIONS:
            1. First seven rows
            2. Last seven rows
            3. View numerical data
            4. View categorical data
            5. Unique column data
            6. Histogram visual of numerical data
            -1. Quit
        ''')
        user_input = int(input('ENTER OPTION: '))

        if user_input == 1: print(first_seven_rows)
        elif user_input == 2: print(last_seven_rows)
        elif user_input == 3: print(numerical_cols)
        elif user_input == 4: print(categorical_cols)
        elif user_input == 5: 
            for col in df.columns:
                print(f'{col}: {pd.Series(df[col]).unique()}\n')
        elif user_input == 6: plt.show()
        else: break

# begins program
csv_exercise()



