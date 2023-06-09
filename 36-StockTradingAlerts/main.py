import os

import requests
import pandas
import json
from twilio.rest import Client

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

STOCK_API_KEY = ""
NEWS_API_KEY = ""

## STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

stock_params = {
    "function": "TIME_SERIES_INTRADAY_EXTENDED",
    "symbol": STOCK_NAME,
    "interval": "60min",
    "slice": "year1month1",
    "apikey": STOCK_API_KEY
}

response = requests.get(STOCK_ENDPOINT, params=stock_params)
if response.status_code != 200:
    print("There was an error getting the Data from the STOCK ENDPOINT")
else:
    # If the request is successful, then we save the data in a temp file
    with open('data_temp.csv', 'w') as f:
        f.write(response.text)

    # We use pandas to read the CSV file
    df = pandas.read_csv('data_temp.csv')

    # We convert the Pandas Dataframe to a JSON data
    json_str = df.to_json(orient='records')

    data_list = json.loads(json_str)

    yesterday_data = data_list[0]
    yesterday_closing_price = yesterday_data['close']
    print(yesterday_closing_price)

    day_before_yestarday_data = data_list[1]
    day_before_yestarday_data_price = day_before_yestarday_data['close']
    print(day_before_yestarday_data_price)

    difference = abs(float(yesterday_closing_price) - float(day_before_yestarday_data_price))
    print(difference)

    #  Work out the percentage difference in price between closing price yesterday and closing price
    #  the day before yesterday.
    diff_percent = (difference / float(yesterday_closing_price)) * 100
    print(diff_percent)

    # If TODO4 percentage is greater than 5 then print("Get News").
    if diff_percent > 0.1:
        ## STEP 2: https://newsapi.org/
        # Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.
        news_params = {
            "apiKey": NEWS_API_KEY,
            "q": COMPANY_NAME
        }
        news_response = requests.get(NEWS_ENDPOINT, params=news_params)
        articles = news_response.json()["articles"]

        # Use Python slice operator to create a list that contains the first 3 articles.
        # Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation
        three_articles = articles[:3]
        print(three_articles)

        ## STEP 3: Use twilio.com/docs/sms/quickstart/python
        # to send a separate message with each article's title and description to your phone number.

        # Create a new list of the first 3 article's headline and description using list comprehension.
        formatted_articles = [f"Headline: {article['title']} \nBrief: {article['description']}" for article in three_articles]

        # TODO 9. - Send each article as a separate message via Twilio.
        # account_sid = os.environ['TWILIO_ACCOUNT_SID']
        # auth_token = os.environ['TWILIO_AUTH_TOKEN']
        client = Client(account_sid, auth_token)

        for article in formatted_articles:
            message = client.messages.create(
                body=article,
                from_='+13613264324',
                to='+50233479094'
            )



# Optional TODO: Format the message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""
