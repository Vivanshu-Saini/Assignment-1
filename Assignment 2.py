import requests
from bs4 import BeautifulSoup
import time

# Headers to mimic a request from a browser
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

# List of categories and their respective URLs
category_urls = {
    "Car Audio": "https://www.amazon.com/s?k=car+audio",
    "Suitcases": "https://www.amazon.com/s?k=suitcases",
    "Games": "https://www.amazon.com/s?k=games",
    "Console Games": "https://www.amazon.com/s?k=console+games",
    "Snacks": "https://www.amazon.com/s?k=snacks",
    "Grooming": "https://www.amazon.com/s?k=grooming",
    "Hand Tools": "https://www.amazon.com/s?k=hand+tools",
    "Tablets": "https://www.amazon.com/s?k=tablets",
    "Smartwatches": "https://www.amazon.com/s?k=smartwatches",
    "Haircare": "https://www.amazon.com/s?k=haircare",
    "Wellness": "https://www.amazon.com/s?k=wellness",
    "Cooking Essentials": "https://www.amazon.com/s?k=cooking+essentials",
    "Office Electronics": "https://www.amazon.com/s?k=office+electronics",
    "Projectors": "https://www.amazon.com/s?k=projectors",
    "Aquatic Supplies": "https://www.amazon.com/s?k=aquatic+supplies",
    "Craft Supplies": "https://www.amazon.com/s?k=craft+supplies",
    "Office Supplies": "https://www.amazon.com/s?k=office+supplies",
    "String Instruments": "https://www.amazon.com/s?k=string+instruments",
    "Vitamins": "https://www.amazon.com/s?k=vitamins",
    "Automotive": "https://www.amazon.com/s?k=automotive",
    "Bedding": "https://www.amazon.com/s?k=bedding",
    "PC Games": "https://www.amazon.com/s?k=pc+games",
    "Gaming Chairs": "https://www.amazon.com/s?k=gaming+chairs",
    "Kids' Clothing": "https://www.amazon.com/s?k=kids+clothing",
    "Travel Organizers": "https://www.amazon.com/s?k=travel+organizers",
    "Baby Clothing": "https://www.amazon.com/s?k=baby+clothing",
    "Gaming Consoles": "https://www.amazon.com/s?k=gaming+consoles",
    "Ayurveda": "https://www.amazon.com/s?k=ayurveda"
}

def scrape_category(url):
    # Fetch the page content
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, "html.parser")

    # Find all product links on the page
    product_links = []
    for link in soup.find_all("a", class_="a-link-normal s-no-outline"):
        href = link.get('href')
        if href:
            product_links.append("https://www.amazon.com" + href)

    return product_links

def scrape_all_categories(category_urls):
    all_product_links = {}
    for category, url in category_urls.items():
        print(f"Scraping category: {category}")
        product_links = scrape_category(url)
        all_product_links[category] = product_links
        time.sleep(2)  # Be polite and avoid hitting the server too hard

    return all_product_links

if _name_ == "_main_":
    all_product_links = scrape_all_categories(category_urls)

    # Output the results
    for category, links in all_product_links.items():
        print(f"\nCategory: {category} - Total Products: {len(links)}")
        for link in links:
            print(link)