tool_flight_search = {
    "type": "function",
    "function": {
        "name": "get_flights",
        "description": "Search for flights in US using the departure city, outbound date, arrival city and return date",
        "parameters": {
            "type": "object",
            "properties": {
                "departure_id": {
                    "type": "string",
                    "descriiption": "The departure city airport code"
                },
                "arrival_id": {
                    "type": "string",
                    "descriiption": "The arrival city airport code"
                },
                "outbound_date": {
                    "type": "string",
                    "descriiption": "The departure date in the date format yyyy-mm-dd"
                },
                "return_date": {
                    "type": "string",
                    "descriiption": "The return date in the date format yyyy-mm-dd"
                }
            },
            "required": ["departure_id", "arrival_id", "outbound_date", "return_date"]
        }
    }
}

list = [tool_flight_search]