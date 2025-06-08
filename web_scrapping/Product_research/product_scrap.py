import requests
from bs4 import BeautifulSoup
from saving_html import fetchAndSaveToFile
import sys

def main():
    query = input("Enter the product you want to search for: ")
    platform = input("where you wanna search for this product (amazon/flipkart): ").strip().lower()
    if platform == "flipkart":
        url = flipkart_search_url(query)
        print(f"Fetching data from: {url}")

    elif platform == "amazon":
        url = amazon_search_url(query)
        print(f"Fetching data from: {url}")

    else:
        print("Enter valid platform!!")
        sys.exit(1)
    fetchAndSaveToFile(url, "search_results.html", max_retries=135)



def parseHtmlFile(path):
    with open(path, "r", encoding="utf-8") as file:
        return BeautifulSoup(file.read(), "html.parser")
    
def amazon_search_url(query):
    base_url = "https://www.amazon.com/s?k"
    query = query.replace(" ", "+")
    return f"{base_url}={query}"

def flipkart_search_url(query):
    base_url = "https://www.flipkart.com/search?q"
    query = query.replace(" ", "+")
    return f"{base_url}={query}"


if __name__ == "__main__":
    main()