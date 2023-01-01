<h1 align="center">
Hi! 👋  Josh here! 🙋🏽‍♂️
</h1>

<h1 align="center">
Simple Forex Trading Bot 
==============================

## Table of Contents
1. [Abstract](#abstract)
2. [Requirements](#requirements)
3. [Getting Started](#getting-started)
    * [Credentials](#Credentials)
    * [Virtual Enviroment and dependencies](#virtual-enviroment-and-dependencies)
        * [For Windows](#For-Windows:)
        * [For Mac OS](#For-Mac-OS:)
4. [Usage](#usage)
    * [Setting up the API's](#setting-up-the-apis)
    * [Conclusion and Future Work](#conclusion-and-future-work)


## Abstract

This project is not so much to make money 💰 (perhaps in the future), but just a simple pet project about how to run your own trading bot, how to make use of RESTful API's and how to do simple data cleaning and data visualisation. I chose the medium of Forex because I think it's a little bit more stable than cryptocurrency and also because Fx might be something that I want to go into the future. 

In this project, I connect to OANDA's database using their API's to create a database of the history of the fx exchange. I then use a very simple strategy, called the Moving Average Crossover. You can read more about it here ( https://howtotrade.com/courses/moving-averages-in-forex/moving-average-crossover/#:~:text=What%20is%20a%20Moving%20Average,Simple%20as%20that!)

Basically, the gist is that by calculating two different moving averages, each time the moving averages "crosses" over each other, it's an indicator to buy/sell. While not a foolproof strategy, it is a pretty simple and powerful strategy, perfect for this pet project.

Following that, the bot automatically makes the trade, and sends a telegram message to me. Pretty simple right? Let's get into it!

## Requirements 

You will need to create an account with Oanda and to have some basic knowledge in Python. 

Go to https://www.oanda.com/sg-en/ and create an account. Oanda is a trading platform and is free to sign up, they also have very useful API's which we will be using for data analysis and backtesting



## Getting Started 
Please ensure that you are in the `Demo` version of your account. To do so, hover under your name in the OANDA main page and you should be able to switch to `Demo`. By default you should be in `Live` and that is not where we want to be until we have developed a profitable trading strategy. 
### Credentials 
Certain credentials we need are 
- Account ID
- API Key

#### To get the Account ID

Navigate to `Manage Funds` and under "V20 Account Number" you should be able to see your account number. Take note of that number for we will be using it later. 
#### To get the API Key

Navigate to the `Manage API Access` button and click on it. In the next page, click on `Generate API Token` and make sure to store the token in a safe place. 

## Virtual Enviroment and dependencies
To run the project, I **highly** recommend you create a virtual environment to self-contain the necessary dependencies required to run the trading bot

### For Windows:
##### To create a virtual environment `virtualenv`:

```console
py -m pip install --user virtualenv
py -m venv .venv
```

##### To activate the virtual environment `.venv`:

```console
.\.venv\Scripts\activate

# check virtual environment activated
 where python
```
##### To install the necessary dependencies within `.venv`:
```console
py -m pip install --no-cache-dir -r requirements.txt
```

### For Mac OS:
##### To create a virtual environment `virtualenv`:
```console
python3 -m pip install --user virtualenv
python3 -m venv .venv
```

To activate the virtual environment `.venv`:

```console
source .venv/bin/activate

# check virtual environment activated
which python
```

##### To install the necessary dependencies within `.venv`:
```console
python3 -m pip install --no-cache-dir -r requirements.txt
```

Now that we have everything sorted, we can clone the repository into your local machine 

```console
git clone https://github.com/Josh9911/Forex-trading-bot.git
```
## Usage

### Setting up the API's
Firstly, over in the `defs.py` file, do enter in the API token and your account ID that we saved earlier on.


##### Changing your own secure information
```python
API_KEY = " < YOUR API KEY> "
ACCOUNT_ID = "111-111-11111111-111 < YOUR ACCOUNT ID >" 
OANDA_URL = "https://api-fxpractice.oanda.com/v3"

SECURE_HEADER = {
    'Authorization': f'Bearer {API_KEY}'
}
```

## Conclusion and Future Work

Write conclusion and future work here












