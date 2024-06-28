from typing import Union

from fastapi import FastAPI

from serpapi import GoogleSearch


from main import promptMistral

app = FastAPI()


@app.get("/")
def read_root():
    response=promptMistral("hello, what can you do?")
    return {"hello, what can you do?": response}

@app.get("/flights")
def get_flights(departure_id: str, arrival_id: str, outbound_date: str, return_date: str):
    params = {
        "api_key": "55b10cd637f5ad7d39c0ef71f860854391c68392cb9fc746a27d55274cee1970",
        "engine": "google_flights",
        "hl": "en",
        "gl": "us",
        "departure_id": departure_id,
        "arrival_id": arrival_id,
        "outbound_date": outbound_date,
        "return_date": return_date,
        "currency": "USD"
    }
    print(params)
    search = GoogleSearc(params)
    results = search.get_dict()
    return results

@app.get("/assistant/flights")
def search_flights(message: str) {
    
}