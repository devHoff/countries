import json
import sys
import requests

ALL_URL = "https://restcountries.com/v3.1/all?fields=name"
NAME_URL = "https://restcountries.com/v3.1/name/"

def request_text(url):
    try:
        r = requests.get(url, timeout=15)
        if r.status_code == 200:
            return r.text
        return None
    except requests.RequestException:
        return None

def parse_json(text: str):
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        return None

def count_countries():
    text = request_text(ALL_URL)
    if not text:
        print("Request failed.")
        return

    data = parse_json(text)
    if not data:
        print("Error parsing response.")
        return

    print("There are", len(data), "countries.")

def country_info(countryname: str):
    url = f"{NAME_URL}{countryname}?fields=name,population,currencies"
    text = request_text(url)
    if not text:
        print("Country not found (or request failed).")
        return

    data = parse_json(text)
    if not data or not isinstance(data, list) or len(data) == 0:
        print("Error parsing country data.")
        return

    country = data[0]

    name = country.get("name", {}).get("common", "N/A")
    population = country.get("population", "N/A")

    currencies = country.get("currencies", {})
    currency_parts = []
    for cur in currencies.values():
        cur_name = cur.get("name", "N/A")
        cur_symbol = cur.get("symbol", "N/A")
        currency_parts.append(f"{cur_name} ({cur_symbol})")

    currency_str = ", ".join(currency_parts) if currency_parts else "N/A"

    print("Country:", name)
    print("Population:", population)
    print("Currency:", currency_str)

def main():
    if len(sys.argv) < 2:
        print("Usage:")
        print("  python countries.py count")
        print("  python countries.py info <COUNTRY_NAME>")
        return

    action = sys.argv[1].lower()

    if action == "count":
        count_countries()
    elif action == "info":
        if len(sys.argv) < 3:
            print("Usage: python countries.py info <COUNTRY_NAME>")
            return
        country_info(" ".join(sys.argv[2:]))
    else:
        print(f"Unknown action: {action}")
        print("Valid actions: count, info")

if __name__ == "__main__":
    main()
