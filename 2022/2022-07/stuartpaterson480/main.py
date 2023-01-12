import PySimpleGUI as sg
import requests
from tkinter import messagebox
import os
import pprint

AV_STOCKS_API_KEY = os.environ.get("AV_STOCKS_API_KEY")
AV_STOCKS_ENDPOINT = "https://www.alphavantage.co/query"


layout = [[sg.Text("Search for the stock price for major companies")], [sg.Button("Search"), sg.InputText("TSLA", key='-IN-')]]

window = sg.Window("Demo", layout)

i = 1
# Create an event loop
while True:
    event, values = window.read()
    # End program if user closes window or
    # presses the OK button

    if event == "Search":

        STOCK = values['-IN-']
        AV_PARAMETERS = {
            "function": "TIME_SERIES_DAILY",
            "symbol": STOCK,
            "apikey": AV_STOCKS_API_KEY
        }
        response = requests.get(url=AV_STOCKS_ENDPOINT, params=AV_PARAMETERS)
        response.raise_for_status()
        data = response.json()
        pp = pprint.PrettyPrinter(indent=4)
        pp.pprint(data)
        daily_data = data['Time Series (Daily)']
        closing_data = [daily_data[key]['4. close'] for key in daily_data]
        price = closing_data[0]
        print(F"Stocks response code: {response.status_code}")
        sg.popup(f"Closing stock price of {STOCK} is ${price}")
    elif event == sg.WIN_CLOSED:
        break

window.close()




