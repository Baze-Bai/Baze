import pandas as pd
import chardet


def process_xlsx(file_path, column_index): #define the function to process the xlsx file
    '''This function reads a csv file and deletes the raws according to the value of given column'''
    df = pd.read_excel(file_path) #read the xlsx file
    df = df.dropna(subset=[df.columns[int(column_index)]]) #delete the raws according to the value of given column
    return df
