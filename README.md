# Real Estate Price Evaluation with Scrapy and Scikit-learn

## Project Description

This project uses **Scrapy** to collect real estate price data from a specific website. After collection, we apply Machine Learning techniques, specifically linear regression models from **Scikit-learn** (Linear Regression, ElasticNetCV, RidgeCV, LassoCV), to evaluate and compare real estate prices. The primary focus is to determine which model offers the lowest error rate (Root Mean Square Error - RMSE) in price prediction.

## Getting Started

The following instructions will help you set up and run the project on your local machine.

### Prerequisites

Before starting, you will need to install the following tools:

- Python 3
- Scrapy
- Scikit-learn
- Pandas
- Numpy

You can install these libraries using `pip`:

```bash
pip install scrapy scikit-learn pandas numpy
```

### Project Setup

To set up the project, clone the repository and install the dependencies:

```bash
git clone https://github.com/mateusbonati/property-price-forecast
cd precos_imoveis
```

## Usage

To start data collection, run the Scrapy spider:

```bash
scrapy crawl imovel
```

After collection, the data will be saved in a database.

## Analysis and Results

The `analise_exploratoria/descritiva.ipynb` script will train regression models with the collected data and compare their RMSEs. The results will help determine the most effective model for predicting real estate prices.


## Representative Image of the Project

![Representative Image](https://github.com/mateusbonati/property-price-forecast/blob/main/model_evaluate.png)
