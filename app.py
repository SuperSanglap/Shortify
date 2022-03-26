from flask import Flask, render_template, request
app = Flask(__name__)
import pyshorteners

@app.route('/')
def home():
	return render_template("index.html")

@app.route('/', methods = ['POST', 'GET'])
def my_form_post():
    url = request.form['text']
    api = request.form['api']
    try:
        if api == 'tinyurl':
            result = tinyurl(url)
        elif api == 'bitly':
            result = bitly(url)
        elif api == 'adfly':
            result = adfly(url)
        elif api == 'isgd':
            result = isgd(url)
        elif api == 'osdb':
            result = osdb(url)
        elif api == 'chilpit':
            result = chilpit(url)
        elif api == 'clckru':
            result = clckru(url)
        elif api == 'dagd':
            result = dagd(url)
    except:
        result = "Something Went Wrong!"

    return render_template("result.html", result = result)

def tinyurl(query):
    shortener = pyshorteners.Shortener()
    shortLink = shortener.tinyurl.short(query)
    return shortLink

def bitly(query):
    shortener = pyshorteners.Shortener(api_key="bcea98de721cdb83cdf8b6fba6ff3a7b12922879")
    shortLink = shortener.bitly.short(query)
    return shortLink

def adfly(query):
    shortener = pyshorteners.Shortener(api_key="3f71fb202d563255e6bc39cd5f6f0063", user_id='19928857', domain='q.gs')
    shortLink = shortener.adfly.short(query)
    return shortLink

def isgd(query):
    shortener = pyshorteners.Shortener()
    shortLink = shortener.isgd.short(query)
    return shortLink

def osdb(query):
    shortener = pyshorteners.Shortener()
    shortLink = shortener.osdb.short(query)
    return shortLink

def chilpit(query):
    shortener = pyshorteners.Shortener()
    shortLink = shortener.chilpit.short(query)
    return shortLink

def clckru(query):
    shortener = pyshorteners.Shortener()
    shortLink = shortener.clckru.short(query)
    return shortLink

def dagd(query):
    shortener = pyshorteners.Shortener()
    shortLink = shortener.dagd.short(query)
    return shortLink

if __name__ == '__main__':
	app.run(debug=True)
