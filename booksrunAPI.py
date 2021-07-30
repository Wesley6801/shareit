import requests
apiKey = '?key=39dai1oqa1s88gfbi06e'
baseBuyURL = "https://booksrun.com/api/v3/price/buy/"

def get_bookPrices_json(isbn):
    if type(isbn) is not str and not int:
        return "Error"
    res = requests.get(baseBuyURL +
                       str(isbn) + apiKey)
    if res.status_code != 200:
        return "Error"
    d = {}
    json = res.json()
    if json['result']['status'] == 'success':
        offers = json['result']["offers"]["booksrun"]
        if isinstance(offers['used'], dict):
            d['price_used'] = offers['used']["price"]
            d['url_used'] = offers['used']['cart_url']
        else:
            d['price_used'] = "No used textbooks."
            d['url_used'] = "No used textbooks."
        if isinstance(offers['new'], dict):
            d['price_new'] = offers['new']['price']
            d['url_new'] = offers["new"]['cart_url']
        else:
            d['url_new'] = "No new textbooks."
            d['price_new'] = "No new textbooks."
        return d  # Returns a dictionary with the used and new price
    return "Error"
# of a textbook. Also the url to redirect to the Booksrun website to purchase.of 


def get_bookPrices(bookname, isbn):
    d = get_bookPrices_json(isbn)
    if d != "Error":
        temp = ""
        price_new = d['price_used'] == "No used textbooks."
        price_used = d['price_new'] == "No new textbooks."
        if not price_new and not price_used:
            temp = "For the book, " + bookname + \
                   ", the used price in Booksrun is $" + \
                   str(d['price_used']) + \
                   ". The new price is $" + str(d['price_new'])
        elif price_used and not price_new:
            temp = "For the book, " + bookname + \
                ", there is only new textbooks in Booksrun. " + \
                "They cost $" + str(d['price_new']) + "."
        elif price_new and not price_used:
            temp = "For the book, " + bookname + \
                ", there is only used textbooks in Booksrun. " + \
                "They cost $" + str(d['price_used']) + "."
        else:
            temp = "There are no results for the book, " + bookname + \
                ", in booksrun."
        return temp
    return "Error"