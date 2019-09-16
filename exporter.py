import os, sys, getopt, datetime, codecs

def saveToFile (file, stockname, since_date, until_date):
    pass
    
def main(argv):
 
    if len(argv) == 0:
        print('You must pass some parameters')
        return

    elif len(argv) == 1 and argv[0] == '-h':
        print('help file')
        return

    try:
        opts, args = getopt.getopt(argv, "", ("ticker=", "fromfile=", "since=", "until="))

        stocks = ''; date_since = ''; date_until = ''
        outputFileName = 'finances.csv'

        for opt, arg in opts:
            
            if opt == '--ticker':
                stocks = [arg]

            elif opt == '--fromfile':
                f = open(arg, "r")

            elif opt == '--since':
                date_since = arg

            elif opt == '--until':
                date_until = arg

    except arg:
        print('Arguments parser error, try -h'+arg)
    finally:
        print('let is go home')

if __name__ == "__main__":
    main(sys.argv[1:])