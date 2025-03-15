import requests
from urllib.parse import urlparse, parse_qs


# Example 1: Using an API to Fetch Weather Data
def fetch_weather_data(city, api_key):
    api_url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'
    response = requests.get(api_url)

    if response.status_code == 200:
        data = response.json()
        print(f"Weather in {city}: {data['weather'][0]['description']}")
        print(f"Temperature: {data['main']['temp']}K")
    else:
        print("Failed to retrieve data")


# Example 2: Understanding and Breaking Down a URL
def break_down_url(url):
    parsed_url = urlparse(url)
    print(f"URL: {url}")
    print(f"Protocol: {parsed_url.scheme}")
    print(f"Domain: {parsed_url.netloc}")
    print(f"Path: {parsed_url.path}")
    print(f"Query: {parsed_url.query}")
    print(f"Fragment: {parsed_url.fragment}")

    if parsed_url.query:
        query_params = parse_qs(parsed_url.query)
        print("Query Parameters:")
        for param, value in query_params.items():
            print(f"{param}: {value}")


# Example 3: Consuming a Public API with Python (Cryptocurrency data)
def fetch_cryptocurrency_data():
    api_url = 'https://api.coingecko.com/api/v3/coins/markets'
    params = {
        'vs_currency': 'usd',
        'ids': 'bitcoin,ethereum,litecoin'
    }
    response = requests.get(api_url, params=params)

    if response.status_code == 200:
        data = response.json()
        print("Cryptocurrency Data:")
        for coin in data:
            print(f"{coin['name']}: ${coin['current_price']}")
    else:
        print("Failed to retrieve data")


# Example 4: API Endpoint in Flask (Conceptual Overview)
from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/weather')
def weather():
    city = 'London'  # Example city
    # Normally, you'd fetch this from an API
    weather_data = {'city': city, 'description': 'Clear Sky', 'temperature': '290K'}
    return jsonify(weather_data)


if __name__ == '__main__':
    app.run(debug=True)


# Example 5: Making an API Call to a URL
def make_api_call():
    url = "https://www.w3schools.com/js/js_api_intro.asp"
    response = requests.get(url)

    if response.status_code == 200:
        print(f"Page content: {response.text[:100]}...")  # Printing first 100 characters
    else:
        print("Failed to retrieve the webpage")


# Run all examples
if __name__ == "__main__":
    print("Fetching weather data...")
    fetch_weather_data('London', 'your_api_key_here')  # Replace with your API key for real data
    print("\nBreaking down a URL...")
    break_down_url('https://www.example.com:8080/path/to/resource?query=python&sort=asc#section2')
    print("\nFetching cryptocurrency data...")
    fetch_cryptocurrency_data()
    print("\nMaking an API call to a website...")
    make_api_call()
