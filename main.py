import Stock as st
import os, sys, getopt, datetime, codecs

def save_to_file(stockNames, outputFileName, sinceDate, untilDate):

    f = open(outputFileName, "w")
    f.write(("%s, %s, %s, %s, %s, %s, %s" % ('Ticker symbol',  'Date', 'Open', 'High', 'Low', 'Adj close', 'Volume')) )

    for stock in stockNames:
        print(stock.date)
        f.write(('%s\n' % (stock, stock.date.date())))

    f.close()

def main():
    file_name = 'stocklist.txt'
    outputFileName = 'financial.csv'
    since = '2019-01-01'
    until = '2019-06-06'

    if os.path.exists(file_name):
        with open(file_name, 'r') as f:
            try:
                list = f.read().splitlines()
                save_to_file(list, outputFileName, since, until)

            except IOError: # whatever reader errors you care about
                print('Could not read file. Check permissions')
            # handle error
    else:
        print(f'file "{file_name}" does not exist in your current directory')

if __name__ == '__main__':
    main()