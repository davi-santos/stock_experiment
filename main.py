import Stock as st
import os, sys, getopt, datetime, codecs
import yfinance as yf
import numpy as np

def main():
    fileName = 'stocklist.txt'
    outputFileName = 'financial.csv'
    since = '2019-01-01'
    until = '2019-06-06'

    if os.path.exists(fileName):
        with open(fileName, 'r') as f:
            try:
                lista = f.read().splitlines()
                words = ' '.join(lista)
                search = yf.download(words, start=since, end=until)
                search.to_csv(outputFileName, header=True, sep='\t', encoding='utf-8')

            except IOError:     
                print('Could not read file. Check permissions')
    else:
        print(f'file "{file_name}" does not exist in your current directory')

if __name__ == '__main__':
    main()