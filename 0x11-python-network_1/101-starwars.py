#!/usr/bin/python3
"""Sends a search request for a given string to the Star Wars API.

Mangages pagination to display all results.

Usage: ./9-starwars.py <search string>
  - The search request is sent to the Star Wars API search people endpoint.
"""
import sys
import requests


if __name__ == "__main__":
    url = "https://swapi.co/api/people/?search={}".format(sys.argv[1])

    r = requests.get(url)
    results = r.json()
    count = results.get("count")
    print("Number of results: {}".format(count))

    c = 0
    while c < count:
        for r in results.get("results"):
            print(r.get("name"))
            c += 1

        next_page = results.get("next")
        if next_page is not None:
            results = requests.get(next_page).json()
