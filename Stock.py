class Stock ():
    def __init__(self, date='', value=''):
        
        self.date = date
        self.value = value
        self.daily_resolution = 0
        
        if date=='':
            raise ValueError("You must assign a date value: yyyy/mm/dd")
        if value=='':
            raise ValueError("You must assign a stock market price")

    def setDailyResolution(self, value):
        self.daily_resolution = float((self.value-value)/self.value)

#get a zip object holding a list of dates and list of stock prices
def stockList(data_items):
    stock_data = [Stock(key, value) for key,value in data_items]
    
    for i in range(1, len(stock_data)):
        stock_data[i].setDailyResolution(stock_data[i-1].value)
    
    return stock_data