import os, sys, getopt, datetime, codecs

def saveToFile (file, stockname, since_date, until_date):

    


def main(argv):
 
    if len(argv) == 0:
        print('You must pass some parameters')
        return

    elif len(argv) == 1 and argv[0] == '-h':
        print('help file')
        return

    try:
        opts, args = getopt.getopt(argv, "", ("stockname=", "stocklist=", "since=", "until="))

        filename = ''; 
        outputFileName = 'stock.csv'

        for opt, arg in opts:
            
            if opt == '--stockname':
                print(f'stockname is {opt}')

            elif opt == '--stocklist':
                print(f'stocklist is {opt}')

            elif opt == '--since':
                print(f'since is {opt}')

            elif opt == '--until':
                print(f'until is {opt}')

    except arg:
        print('Arguments parser error, try -h'+arg)
    finally:
        print('let is go home')

if __name__ == "__main__":
    main(sys.argv[1:])