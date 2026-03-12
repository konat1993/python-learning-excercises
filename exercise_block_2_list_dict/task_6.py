# Task 6: Create a dictionary of countries and their capitals and print them.

countries = {
    "Poland": {"capital": "Warsaw"},
    "Germany": {"capital": "Berlin"},
    "Spain": {"capital": "Madrid"},
    "Italy": {"capital": "Rome"},
    "France": {"capital": "Paris"},
}

for country, country_details in countries.items():
    print(f"Country: {country}")
    print(f"Capital: {country_details['capital']}")
    print("--------------------------------")
