from datetime import date, timedelta
from nsetools import Nse
from nsepy import get_history
import time
from html_template import main_body, table_row
import csv

# Calculate first day, last day, month and year for previous month
last_day_of_prev_month_data = date.today().replace(day=1) - timedelta(days=1)
start_day_of_prev_month_data = date.today().replace(day=1) - timedelta(days=last_day_of_prev_month_data.day)
first_day = start_day_of_prev_month_data.day
last_day = last_day_of_prev_month_data.day
month = start_day_of_prev_month_data.month
year = start_day_of_prev_month_data.year

# Get stocks from CSV file. The file must contain only one column with only stock names.
# There shouldn't be any heading such as "Symbol", "Quotes" etc. because it will throw
# an exception.
try:
    file = open('stock_data.csv')
    csv_reader = csv.reader(file)
except:
    print("Please ensure that stock_data.csv file is present in the same directory as the python script.")
    input("Press any key to exit...")
    exit()

stocks = []

for row in csv_reader:
    stocks.extend(row)
file.close()

nse = Nse()

table_data = ""

for stock in stocks:
    try:
        # Get stock data using NSEPy and NSETools
        print("Getting data for ", stock)
        current_price = nse.get_quote(stock)["lastPrice"]
        # Get price of the stock (close, high, low) for each day for previous month
        quote_history = get_history(symbol=stock,
                           start=date(year, month, first_day),
                           end=date(year , month, last_day))
        # Closing price of the stock is the closing price on the last day of previous month
        close = quote_history["Close"].to_list().pop()
        # Get the price of stock for first day of previous month. This data is later
        # used to calculate the trend on monthly basis.
        previous_month_price = quote_history["Close"].to_list()[0]
        high = max(quote_history["High"].to_list())
        low = min(quote_history["Low"].to_list())
    except:
        print(stock, " might be not be present in NIFTY. Or there might be some change in the Symbol name on NSE. Please verify. Continuing")
        continue

    # Calculate top central pivot, bottom central pivot and centra pivot
    cp = (high + low + close) / 3
    bc = (high + low) / 2
    tc = cp + (cp - bc)
    top_central = round(tc, 2) if (tc > bc) else round(bc, 2)
    bottom_central = round(bc, 2) if (bc < tc) else round(tc, 2)
    central = round(cp, 2)

    # Calculate the offset range. It will be slightly higher than the top central pivot. 1.5% of the stock price is
    # calculated as offset
    upper_range = top_central + ((1.5/100) * top_central)

    trend = ""
    trend_color = ""

    probability = ""
    probability_color = ""

    if int(current_price) in range(int(bottom_central), int(upper_range)):
        # Determine the Trend
        if previous_month_price > current_price:
            trend = "DOWN"
            trend_color = "red"
        else:
            trend = "UP"
            trend_color = "green"
        # Determine the bullish probability
        if int(current_price) in range(int(bottom_central), int(central)):
            probability = "LOW"
            probability_color = "red"
            print(stock, " has ", probability, " probability")
        elif int(current_price) in range(int(central), int(top_central)):
            probability = "MEDIUM"
            probability_color = "black"
            print(stock, " has ", probability, " probability")
        elif int(current_price) in range(int(top_central), int(upper_range)):
            probability = "HIGH"
            probability_color = "green"
            print(stock, " has ", probability, " probability")
        # Appending the row data including stock name, price, trend and probability to the main HTML template body
        new_table_row = table_row.format(stock, str(current_price), trend_color, trend, probability_color, probability)
        table_data = table_data + new_table_row + "\n"
    # In order to avoid being blocked by the server, we keep a time interval of 6 seconds between each request.
    time.sleep(6)
# Final HTML template
final_html_body = main_body
final_html_body = final_html_body.format(table_data)
print("Generating report")
with open('stock_picks.html', "w") as my_file:
    my_file.write(final_html_body)
input("Analysis complete. Please refer stock_picks.html...")