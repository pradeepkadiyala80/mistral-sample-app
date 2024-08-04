import json
import os
import logging

# Get the existing logger
logger = logging.getLogger('my_logger')

from serpapi import GoogleSearch

g_api_key = os.getenv("GOOGLE_SEARCH_APIKEY")

def get_flights(departure_id: str, arrival_id: str, outbound_date: str, return_date: str):    
    params = {
        "api_key": g_api_key,
        "engine": "google_flights",
        "hl": "en",
        "gl": "us",
        "departure_id": departure_id,
        "arrival_id": arrival_id,
        "outbound_date": outbound_date,
        "return_date": return_date,
        "currency": "USD"
    }
    logger.info(params)
    search = GoogleSearch(params)
    results = search.get_dict()
    return results
