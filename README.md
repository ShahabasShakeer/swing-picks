# Swing Picks
Python stock selection script for Swing trading using CPR strategy.

## Overview
CPR is a leading indicator in the stock market. Many stocks do tend to reverse in the vicinity of CPR. This makes it a good indicator for stock selection and buy signals.

In this script, Monthly CPR is calculated because the stocks are selected for Swing Trading. Day candles must be used while analysing the stock picked by the script.

Each stock is analysed keeping a time interval of 6 seconds. This is done in order to avoid being blocked by NSE due to lots of simultaneous requests.

## How to Use

- Edit the stock_data.csv file. Add the stocks that you would like to analyse in the first column. Please do not modify any other columns.
- Run the script.

## Requirements
You need to install nsetools and nsepy to get data NIFTY stock data.

## Disclaimer
Stock trading is inherently risky and the users agree to assume complete and full responsibility for the outcomes of all trading decisions that they make, including but not limited to loss of capital. Under no circumstances should any user make trading decisions based solely on the information generated from the application.
