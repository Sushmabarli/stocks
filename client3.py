################################################################################
#
#  Permission is hereby granted, free of charge, to any person obtaining a
#  copy of this software and associated documentation files (the "Software"),
#  to deal in the Software without restriction, including without limitation
#  the rights to use, copy, modify, merge, publish, distribute, sublicense,
#  and/or sell copies of the Software, and to permit persons to whom the
#  Software is furnished to do so, subject to the following conditions:
#
#  The above copyright notice and this permission notice shall be included in
#  all copies or substantial portions of the Software.
#
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
#  OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
#  FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
#  DEALINGS IN THE SOFTWARE.

import json
import random
import urllib.request

# Server API URLs
QUERY = "http://localhost:8080/query?id={}"

# 500 server request
N = 500


def getDataPoint(quote):
    """ Produce all the needed values to generate a datapoint """
    stock = quote['stock']
    bid_price = float(quote['top_bid']['price'])
    ask_price = float(quote['top_ask']['price'])
    price = (bid_price + ask_price) / 2
    return stock, bid_price, ask_price, price


def getRatio(price_a, price_b):
    """ Get ratio of price_a and price_b """
    ratio = price_a / price_b
    return ratio


# Main
if __name__ == "__main__":
    # Query the price once every N seconds.
    for _ in iter(range(N)):
        quotes = json.loads(urllib.request.urlopen(QUERY.format(random.random())).read())

        # Process the data for stock A and stock B
        stock_a_data = None
        stock_b_data = None

        for quote in quotes:
            stock, bid_price, ask_price, price = getDataPoint(quote)

            if stock == 'StockA':
                stock_a_data = (stock, bid_price, ask_price, price)
            elif stock == 'StockB':
                stock_b_data = (stock, bid_price, ask_price, price)

        if stock_a_data and stock_b_data:
            stock_a, bid_a, ask_a, price_a = stock_a_data
            stock_b, bid_b, ask_b, price_b = stock_b_data

            print("Stock A: %s (Bid: %.2f, Ask: %.2f, Price: %.2f)" % (stock_a, bid_a, ask_a, price_a))
            print("Stock B: %s (Bid: %.2f, Ask: %.2f, Price: %.2f)" % (stock_b, bid_b, ask_b, price_b))

            ratio = getRatio(price_a, price_b)
            print("Ratio: %.2f" % ratio)
