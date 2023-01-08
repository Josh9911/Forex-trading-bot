<h1 align="center">
Hi! 👋  Josh here! 🙋🏽‍♂️
</h1>

<h1 align="center">
Forex-API-Pipeline

## Table of Contents
1. [Abstract](#abstract)
2. [Requirements](#requirements)
3. [Getting Started](#getting-started)
    * [Oanda](#Oanda)
    * [Amazon Web Services](#amazon-web-services-aws)
    * [Virtual Enviroment and dependencies](#virtual-enviroment-and-dependencies)
4. [Usage](#usage)
    * [Setting up the API's](#setting-up-the-apis)
    * [Conclusion and Future Work](#conclusion-and-future-work)


## Abstract

This project is not so much to make money 💰 (perhaps in the future), but just a simple pet project motivated by my interest in data engineering. This is for me to develop my skills and experience on the tools of the trade and as such, the project is a little "overkill" as I make use of `Airflow`, `Docker`, `Amazon S3 and Redshift` and data visualisation tools such as `Google Data Studio`. I chose the topic of Forex because I think it's something that someone might want to use and also it might be something that I would to get into the future. 

In this project, I connect to OANDA's database using their API's to create a database of the history of the fx exchange.


## Requirements 

I am currently running this on a Macbook Pro 2020 (Intel Chip) with 16GB of Ram.

- Install [Python](https://www.python.org/)
- Install your favourite IDE, personally I like to use [Visual Studio Code](https://code.visualstudio.com/)

## Getting Started 
 
### Oanda
You will need to create an account with Oanda and to have some basic knowledge in Python. 

Go to [Oanda](https://www.oanda.com/sg-en/) and create an account. Oanda is a trading platform and is free to sign up, they also have very useful API's which we will be using for data analysis and backtesting

Please ensure that you are in the `Demo` version of your account. To do so, hover under your name in the OANDA main page and you should be able to switch to `Demo`. By default you should be in `Live` and that is not where we want to be until we have developed a profitable trading strategy.

Certain credentials we need are 
- Account ID
- API Key

#### To get the Account ID

Navigate to `Manage Funds` and under "V20 Account Number" you should be able to see your account number. Take note of that number for we will be using it later. 
#### To get the API Key

Navigate to the `Manage API Access` button and click on it. In the next page, click on `Generate API Token` and make sure to store the token in a safe place. 

### Amazon Web Services (AWS)

We'll be using the cloud to store our Forex data; specifically, Amazon Web Service (AWS) which offers a free tier.

We will be using two of their services:

* [Simple Storage Service (S3)](https://aws.amazon.com/s3/)  ~ This is Object Storage. When we extract data from Oanda, we'll store it in a CSV and push to an S3 Bucket as an object. This allows us to store all our raw data in the cloud.

* [Redshift](https://aws.amazon.com/redshift/) ~ This is a Data Warehousing service. Utilising its Massively Parallel Processing (MPP) technology, Redshift is able to execute operations on large datasets at fast speeds. It's based on PostgreSQL, so we can use SQL to run operations here. It is pretty expensive but we it should be fine for a small project like this.

To get started with AWS, follow the below steps:

#### Setup

1. Setup a personal [AWS account](https://portal.aws.amazon.com/billing/signup?nc2=h_ct&src=header_signup&redirect_url=https%3A%2F%2Faws.amazon.com%2Fregistration-confirmation#/start). Follow instructions [here](https://aws.amazon.com/getting-started/guides/setup-environment/module-one/) and setup with free tier.

2. Secure your account following these [steps](https://aws.amazon.com/getting-started/guides/setup-environment/module-two/). 

    Here we are setting up MFA for the root user. The root is a special account that has access to everything. Therefore it's important we secure this. Also be sure to setup an IAM user which will have its own set of permissions, in this case, admin permissions. Generally in production, you should only use the root account for tasks that can only be done with the root account.

3. Setup CLI following this [guide](https://aws.amazon.com/getting-started/guides/setup-environment/module-three/). 

    This allows us to control AWS services from the command line interface. The goal by the end of this is you should have a folder in your home directory called `.aws` which contains a `credentials` file. It will look something like this:

    ```config
    [default]
    aws_access_key_id = XXXX
    aws_secret_access_key = XXXX
    ```

    This will allow our scripts to interact with AWS without having to include our access key and secret access key within the scripts.
## Virtual Enviroment and dependencies
To run the project, I **highly** recommend you create a virtual environment to self-contain the necessary dependencies required to run the trading bot

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

## Future Work
Using a very simple strategy, called the Moving Average Crossover to automate trades. You can read more about it here ( https://howtotrade.com/courses/moving-averages-in-forex/moving-average-crossover/#:~:text=What%20is%20a%20Moving%20Average,Simple%20as%20that!)


Basically, the gist is that by calculating two different moving averages, each time the moving averages "crosses" over each other, it's an indicator to buy/sell. While not a foolproof strategy, it is a pretty simple and powerful strategy, perfect for this pet project.













