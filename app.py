from flask import Flask, render_template, request, redirect
app = Flask(__name__)
import pyshorteners

@app.route('/')
def home():
	return render_template("index.html")

@app.route('/', methods = ['POST', 'GET'])
def my_form_post():
    url = request.form['text']
    api = request.form['api']
    if api == 'tinyurl':
        result = tinyurl(url)
    elif api == 'bitly':
        result = bitly(url)
    elif api == 'adfly':
        result = adfly(url)

    return render_template("result.html", result = result)

def tinyurl(query):
	try:
		shortener = pyshorteners.Shortener()
		shortLink = shortener.tinyurl.short(query)
	except:
		shortLink = ""
	return shortLink

def bitly(query):
    try:
        shortener = pyshorteners.Shortener(api_key="bcea98de721cdb83cdf8b6fba6ff3a7b12922879")
        shortLink = shortener.bitly.short(query)
    except:
        shortLink = ""
    return shortLink

def adfly(query):
    try:
        shortener = pyshorteners.Shortener(api_key="3f71fb202d563255e6bc39cd5f6f0063", user_id='19928857', domain='q.gs')
        shortLink = shortener.adfly.short(query)
    except:
        shortLink = ""
    return shortLink

if __name__ == '__main__':
	app.run(debug=True)
