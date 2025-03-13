import os
import time
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd

# Setup output directory
output_folder = "output"
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Configure Selenium WebDriver
chrome_options = Options()
chrome_options.add_argument("--headless")  # Run Chrome in headless mode
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--window-size=1920x1080")
chrome_options.add_experimental_option("detach", True)
chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])

# Initialize WebDriver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

def scrape_product_data(url):
    """Scrapes product data from a given URL"""
    driver.get(url)
    time.sleep(2)  # Wait for page to load

    soup = BeautifulSoup(driver.page_source, "html.parser")

    try:
        title = soup.find("h1", class_="product-title").text.strip()
    except AttributeError:
        title = "N/A"

    try:
        price = soup.find("span", class_="product-price").text.strip()
    except AttributeError:
        price = "N/A"

    try:
        description = soup.find("div", class_="product-description").text.strip()
    except AttributeError:
        description = "N/A"

    return {
        "Title": title,
        "Price": price,
        "Description": description,
        "URL": url
    }

# List of product URLs
product_urls = [
    "https://example.com/product1",
    "https://example.com/product2",
    "https://example.com/product3"
]

product_data = []

for url in product_urls:
    print(f"Scraping: {url}")
    product_data.append(scrape_product_data(url))

driver.quit()

# Save to Excel
output_file = os.path.join(output_folder, "ecommerce_products.xlsx")
df = pd.DataFrame(product_data)
df.to_excel(output_file, index=False)

print(f"Data saved successfully at: {output_file}")




