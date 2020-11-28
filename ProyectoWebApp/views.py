from django.shortcuts import render
import yfinance as yf
import datetime

# Create your views here.


def index(request):

    tickers = ['AAPL', 'MELI', 'TSLA', 'AMZN', 'FB', 'GOOG', 'NFLX']
    tickersarg = ['AAPL.BA', 'MELI.BA', 'TSLA.BA', 'AMZN.BA', 'FB.BA', 'GOOGL.BA', 'NFLX.BA']
    ratio = [10, 60, 15, 144, 8, 58, 16]
    datos = []
    i = 0
    r = 0
    today = datetime.date.today()
    yesterday = today - datetime.timedelta(days=1)

    for symbol in tickers:

        data = yf.download(tickers[i], auto_adjust=True, start=today)['Close']
        dataarg = yf.download(tickersarg[i], auto_adjust=True, start=today)['Close']
        y_data = yf.download(tickers[i], auto_adjust=True, start=yesterday)['Close']
        y_dataarg = yf.download(tickersarg[i], auto_adjust=True, start=yesterday)['Close']
        ccl = round((dataarg[0] / data[0]) * (ratio[r]), 2)
        y_ccl = round((y_dataarg[0] / y_data[0]) * (ratio[r]), 2)
        variacion = round(ccl-y_ccl, 2)

        info = {
            'tickers': tickers[i],
            'ccl': ccl,
            'variacion': variacion
        }
        i += 1
        r += 1
        datos.append(info)
        print(ccl)

    context = {'datos': datos}
    #print(context)

    return render(request, 'root/index.html', context)
