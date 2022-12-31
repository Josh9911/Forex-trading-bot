<h1 align="center">
Hi! 👋  Josh here! 🙋🏽‍♂️
</h1>

<h1 align="center">
Simple Forex Trading Bot 
==============================

## Table of Contents
1. [Abstract](#abstract)
2. [Requirements](#requirements)
    * Creating a Virtual Enviroment
        * [For Windows](#For-Windows:)
        * [For Mac OS](#For-Mac-OS:)
3. [Getting Started](#getting-started)
    * [Credentials](#Credentials)
4. [Project Overview](#project-overview)
    * [Conclusion and Future Work](#conclusion-and-future-work)
5. [Project Organisation](#project-organisation)

## Abstract

Write Abstract here 

## Requirements 

You will need to create an account with Oanda and to have some basic knowledge in Python. 

Go to https://www.oanda.com/sg-en/ and create an account. Oanda is a trading platform and is free to sign up, they also have very useful API's which we will be using for data analysis and backtesting

To run the project, I **highly** recommend you create a virtual environment to self-contain the necessary dependencies required to run the trading bot


## For Windows:
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

## For Mac OS:
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














