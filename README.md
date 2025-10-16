# Project-3

## Introduction

The goal of this project is to apply the Stock-to-Flow (S2F) model to predict the price of Ethereum (ETH), the second-largest cryptocurrency by market capitalization. The Stock-to-Flow model, originally used for analyzing commodities like gold and Bitcoin, relates the existing stock (total supply) of an asset to its flow (annual production or issuance rate) to estimate its potential market value over time.

## Data Pre-Processing

For this project, I performed several data preprocessing steps to prepare the Ethereum dataset for analysis. I first collected daily historical price data using the Yahoo Finance API and extracted only the necessary columns such as date and closing price. The date column was then converted into a datetime format and grouped by year to estimate annual values. Next, I engineered new features to represent Ethereum’s stock (total supply), flow (newly issued ETH), and the Stock-to-Flow (S2F) ratio, which measures scarcity. Missing values created during differencing were handled using backward filling to maintain data continuity. To linearize the power-law relationship between scarcity and price, both the S2F ratio and price were log-transformed before applying regression. Finally, rows with missing or invalid values were removed to ensure a clean and consistent dataset for modeling.

## Evaluation