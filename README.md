# mistral-sample-app

This is a sample application that will act as a travel agent to find flights with price tag

# Pre-Requisites

### 1. Get API Keys and export them as environment variables

- MISTRAL_API_KEY - Get Mistral apikey from https://mistral.ai/ 

`export MISTRAL_API_KEY=<Mistral API Key>`

- DLAI_MISTRAL_API_ENDPOINT: 

`export DLAI_MISTRAL_API_ENDPOINT="https://api.mistral.ai/v1/chat/completions" `

- GOOGLE_SEARCH_APIKEY: https://serpapi.com/

`export GOOGLE_SEARCH_APIKEY=<SERP API Key> `

### 2. Install Python with version 3.12 and above


# How to run the program?

Step 1: Install the dependency packages from the requirements.txt

`pip install pipreqs`

Step 2: Run the program

`python main.py`

# Example

`> python main.py`
```
Prompt: Find flight from AUS to SAN. I will be traveling on 2024-09-11 and will return on 2024-09-17
Based on your search, here are some flights from Austin (AUS) to San Diego (SAN) for the dates of September 11, 2024, to September 17, 2024:

1. Alaska Airlines, Flight AS 343. Departure from AUS at 07:15, arrival at SAN at 08:20. Duration: 185 minutes. Price: $157.
2. Southwest Airlines, Flight WN 3726. Departure from AUS at 09:00, arrival at SAN at 09:55. Duration: 175 minutes. Price: $158.
3. Southwest Airlines, Flight WN 2283. Departure from AUS at 13:20, arrival at SAN at 14:15. Duration: 175 minutes. Price: $158.

These flights are non-stop and have different legroom options. The Alaska Airlines flight has an average legroom of 31 inches, while the Southwest Airlines flights have an average legroom of 31 inches and above average legroom of 32 inches, respectively.

Please note that the price includes only the base fare and may not include additional fees for checked baggage or other services. The carbon emissions for these flights are lower than the typical emissions for this route, which is a positive environmental impact.

If you're open to flights with layovers or looking for different price options, I can also provide those details.
```



