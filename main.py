import argparse
import pandas as pd
from xlsx_processor import process_xlsx

def main():
    '''This is the main function, which reads the arguments from the command line, processes the csv file and saves the processed csv file to the original file path'''
    parser = argparse.ArgumentParser(description="process csv file, delete the raws according to the value of given column") #read the arguments from the command line
    parser.add_argument('file_path', type=str, help="the path of csv file") #load the path of the xlsx file
    parser.add_argument('column_index', type=str, help="the column name of the csv file") #load the column index

    args = parser.parse_args() #deliver the arguments to args

    df = process_xlsx(args.file_path, args.column_index) #process the xlsx file through the function
    df.to_excel(args.file_path, index=False) #save the processed xlsx file to the original file path




























