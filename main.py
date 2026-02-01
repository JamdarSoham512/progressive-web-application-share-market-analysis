from flask import Flask, render_template
import yfinance as yf
import pandas as pd

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('frontpage.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/team')
def team():
    return render_template('team.html')

@app.route('/livechat')
def livechat():
    return render_template('rel.html')

@app.route('/axis')
def axis():
    stock = yf.Ticker("AXISBANK.NS")
    data = stock.history(period="1d")
    return render_template('axis.html', 
                         price=round(data['Close'].iloc[-1], 2),
                         volume=data['Volume'].iloc[-1])

@app.route('/hdfcbank')  # Changed from '/hdfc' to '/hdfcbank'
def hdfcbank():         # Changed function name from 'hdfc' to 'hdfcbank'
    stock = yf.Ticker("HDFCBANK.NS")
    data = stock.history(period="1d")
    return render_template('hdfcbank.html', 
                         price=round(data['Close'].iloc[-1], 2),
                         volume=data['Volume'].iloc[-1])

@app.route('/reliance')
def reliance():
    stock = yf.Ticker("RELIANCE.NS")
    data = stock.history(period="1d")
    return render_template('reliance.html', 
                         price=round(data['Close'].iloc[-1], 2),
                         volume=data['Volume'].iloc[-1])

@app.route('/tatam')  # Changed from '/tata' to '/tatam' to match template
def tatam():         # Changed function name from 'tata' to 'tatam'
    stock = yf.Ticker("TATAMOTORS.NS")
    data = stock.history(period="1d")
    return render_template('tatam.html', 
                         price=round(data['Close'].iloc[-1], 2),
                         volume=data['Volume'].iloc[-1])

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
