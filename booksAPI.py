import requests
apiKey = '?key=39dai1oqa1s88gfbi06e'
baseBuyURL = "https://booksrun.com/api/v3/price/buy/"
baseGoURL = 'https://www.googleapis.com/books/v1/volumes?q=isbn:'

isbn = 9781284140996


def get_bookPrices_json(isbn):
    if not isinstance(isbn, str) and not int:
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
# of a textbook. Also the url to redirect to the Booksrun website to
# purchase.of


def get_bookPrices(bookname, json):
    if not isinstance(json, dict):
        return ["Error", "Error"]
    d = json
    if d != "Error":
        temp = ""
        url = ""
        price_used = d['price_used'] == "No used textbooks."
        price_new = d['price_new'] == "No new textbooks."
        if not price_new and not price_used:
            temp = "For the book, " + bookname + \
                   ", the used price in Booksrun is $" + \
                   str(d['price_used']) + \
                   ". The new price is $" + str(d['price_new'])
            url = "For the used textbook go to : " + \
                d['url_used'] + "\n" + \
                "For the new textbook go to : " + \
                d['url_new']
        elif price_used and not price_new:
            temp = "For the book, " + bookname + \
                ", there is only new textbooks in Booksrun. " + \
                "They cost $" + str(d['price_new']) + "."
            url = "For the new textbook go to : " + \
                d['url_new']
        elif price_new and not price_used:
            temp = "For the book, " + bookname + \
                ", there is only used textbooks in Booksrun. " + \
                "They cost $" + str(d['price_used']) + "."
            url = "For the used textbook go to : " + \
                d['url_used']
        else:
            temp = "There are no results for the book, " + bookname + \
                ", in booksrun."
            url = ""

        return [temp, url]
    return ["Error", "Error"]


def get_bookImage(isbn):
    if not isinstance(isbn, str) and not int:
        return "Error"
    json = requests.get(baseGoURL + str(isbn)).json()
    if json['totalItems'] <= 0:
        return "Error no images for the book."
    items = json['items'][0]['volumeInfo']
    isbn1 = items["industryIdentifiers"][1]["identifier"]
    isbn2 = items["industryIdentifiers"][0]["identifier"]
    if isbn1 != str(isbn) and isbn2 != str(isbn):
        return "No Book returned"
    else:
        return items["imageLinks"]['thumbnail']
