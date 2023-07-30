# File that includes all the request logic.
import requests
import re
from flask import jsonify


def get_dollar_conversion(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return {"data": response.json()}
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return {"Message": "There was an error on the request."}


def get_dollar_conversion_by_date(url, date='', source=''):
    date_pattern = r"^\d{4}-\d{2}-\d{2}$"
    valid_sources = ["Oficial", "Blue"]
    try:
        if not date or not (re.match(date_pattern, date)):
            data = {
                "Message": "The date is missing."
            } if not date else {
                "Message": "The date provided is invalid, expected format: YYYY-MM-DD."
            }
            response = jsonify(data)
            response.status_code = 400
            return response

        print('.. Getting historic data ..')

        response = requests.get(url)
        response.raise_for_status()
        record = response.json()
        # Filter mathing record by date
        if not source:
            filtered_record = next(
                index for index, d in enumerate(record)
                if d["date"] == date
            ) or None
            return {"data": record[filtered_record]}
        else:
            # TODO: validate source input types and add in bot responses average property.
            filtered_record = next(
                index for index, d in enumerate(record)
                if d["date"] == date and d["source"] == source
            ) or None
            return {"data": record[filtered_record]}
        # Catch non-date record match.
    except StopIteration:
        data = {"Message": "There are not valid records for the date: " + date}
        response = jsonify(data)
        response.status_code = 404
        return response
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        data = {"Message": "There was an error on the request."}
        response = jsonify(data)
        response.status_code = 500
        return response
