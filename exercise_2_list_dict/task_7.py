# Task 7: Sort the countries by country name and print them.

countries = {
    "Poland": {"capital": "Warsaw"},
    "Germany": {"capital": "Berlin"},
    "Spain": {"capital": "Madrid"},
    "Italy": {"capital": "Rome"},
    "France": {"capital": "Paris"},
}

# sorted_countries = sorted(countries.items(), key=lambda x: x[0])

# for country in sorted_countries:
#     print(f"Country: {country[0]}")
#     print(f"Capital: {country[1]['capital']}")
#     print("--------------------------------")

sorted_countries = dict(sorted(countries.items()))
print(sorted_countries)

for country in sorted_countries:
    print(f"Country: {country}")
    print(f"Capital: {sorted_countries[country]['capital']}")
    print("--------------------------------")
