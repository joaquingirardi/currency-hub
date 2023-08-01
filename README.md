# Project Name: CurrencyHub API

This project is a Flask-based backend API that provides endpoints to fetch currency conversion data for the US Dollar (USD) with the Argentine peso (ARS). It uses external APIs to retrieve real-time and historical exchange rate data for the US Dollar.

## Installation and Setup

1. Clone the repository.
2. Install dependencies (make sure you have Python and virtual environment installed):

- python -m venv venv
- source venv/bin/activate # On Windows, use "venv\Scripts\activate"
- pip install -r requirements.txt


## Running the API

To run the API locally, execute the following command from the project root directory:

**python run.py**


The API server will start, and you can access it at `http://127.0.0.1:5000/`.

## Endpoints

### 1. `/`

This endpoint returns a simple "Hello, World!" message to check if the API is running.

### 2. `/dollar`

This endpoint provides the real-time conversion rate for the US Dollar (USD) against a base currency. It fetches the data from the external USD API.

### 3. `/dollar-date`

This endpoint allows you to get historical conversion rates for the US Dollar (USD) against a base currency for a specific date. It takes the following query parameters:

- `date`: The date for which you want the historical conversion rate. Format: `YYYY-MM-DD`.
- `source` (optional): The base currency for the conversion. If not specified, the default base currency is used.

## API Configuration

The API relies on two external API endpoints to fetch currency conversion data:

1. `USD_API_PATH`: This environment variable should be set to the URL of the real-time USD conversion API.

2. `HISTORICAL_USD_API_PATH`: This environment variable should be set to the URL of the historical USD conversion API.

Please ensure that you set these environment variables before running the API to ensure proper functionality.

## Notes

- This project uses Flask and Flask Blueprints to organize the routes and logic for the API.

- The `utils.py` module contains functions to fetch data from the external APIs and handle the currency conversion logic.

- The API follows RESTful principles, providing simple and intuitive endpoints for currency conversion data.

Feel free to explore and use the API to get real-time and historical USD conversion rates!

## Author

Created by - [Joaquin Girardi](https://github.com/joaquingirardi)
