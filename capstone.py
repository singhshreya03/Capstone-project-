#!/usr/bin/env python
# coding: utf-8

# In[2]:


pip install bs4 requests pandas


# In[7]:


import requests
from bs4 import BeautifulSoup
import pandas as pd

# Example function to scrape a single page
def scrape_vestapreferred_page(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    listings = []
    for listing in soup.select('.listing-class'):  # Adjust the class to match the site
        address = listing.select_one('.address-class').text
        city = listing.select_one('.city-class').text
        price = listing.select_one('.price-class').text
        beds = listing.select_one('.beds-class').text
        baths = listing.select_one('.baths-class').text
        sqft = listing.select_one('.sqft-class').text
        listing_url = listing.select_one('a')['href']
        
        listings.append({
            'address': address,
            'city': city,
            'price': price,
            'beds': beds,
            'baths': baths,
            'sqft': sqft,
            'url': listing_url
        })
    
    return listings


url = 'https://vestapreferred.com/'
data = scrape_vestapreferred_page(url)

# Save to a DataFrame
df = pd.DataFrame(data)
df.to_csv('vestapreferred_listings.csv', index=False)


# In[8]:


pip install requests beautifulsoup4 selenium pandas


# In[21]:


import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pandas as pd
import time

# Function to initialize Selenium WebDriver
def init_driver():
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')  # Run in headless mode
    driver = webdriver.Chrome(options=options)
    return driver

# Scrape from Vesta Preferred Realty (Example)
def scrape_vestapreferred(driver, url):
    driver.get(url)
    time.sleep(3)  # Wait for the page to load
    
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    listings = []
    for listing in soup.select('.listing-class'):  # Adjust the class to match the site
        address = listing.select_one('.address-class').text.strip()
        city = listing.select_one('.city-class').text.strip()
        price = listing.select_one('.price-class').text.strip()
        beds = listing.select_one('.beds-class').text.strip()
        baths = listing.select_one('.baths-class').text.strip()
        sqft = listing.select_one('.sqft-class').text.strip()
        listing_url = listing.select_one('a')['href']
        
        listings.append({
            'address': address,
            'city': city,
            'price': price,
            'beds': beds,
            'baths': baths,
            'sqft': sqft,
            'url': listing_url
        })
    return listings

def scrape_Redfin(driver, url):
    driver.get(url)
    time.sleep(3)  # Wait for the page to load
    
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    listings = []
    for listing in soup.select('.listing-class'):  # Adjust the class to match the site
        address = listing.select_one('.address-class').text.strip()
        city = listing.select_one('.city-class').text.strip()
        price = listing.select_one('.price-class').text.strip()
        beds = listing.select_one('.beds-class').text.strip()
        baths = listing.select_one('.baths-class').text.strip()
        sqft = listing.select_one('.sqft-class').text.strip()
        listing_url = listing.select_one('a')['href']
        
        listings.append({
            'address': address,
            'city': city,
            'price': price,
            'beds': beds,
            'baths': baths,
            'sqft': sqft,
            'url': listing_url
        })
    return listings

def scrape_Trulia(driver, url):
    driver.get(url)
    time.sleep(3)  # Wait for the page to load
    
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    listings = []
    for listing in soup.select('.listing-class'):  # Adjust the class to match the site
        address = listing.select_one('.address-class').text.strip()
        city = listing.select_one('.city-class').text.strip()
        price = listing.select_one('.price-class').text.strip()
        beds = listing.select_one('.beds-class').text.strip()
        baths = listing.select_one('.baths-class').text.strip()
        sqft = listing.select_one('.sqft-class').text.strip()
        listing_url = listing.select_one('a')['href']
        
        listings.append({
            'address': address,
            'city': city,
            'price': price,
            'beds': beds,
            'baths': baths,
            'sqft': sqft,
            'url': listing_url
        })
    return listings




def scrape_Point2Homes(driver, url):
    driver.get(url)
    time.sleep(3)  # Wait for the page to load
    
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    listings = []
    for listing in soup.select('.listing-class'):  # Adjust the class to match the site
        address = listing.select_one('.address-class').text.strip()
        city = listing.select_one('.city-class').text.strip()
        price = listing.select_one('.price-class').text.strip()
        beds = listing.select_one('.beds-class').text.strip()
        baths = listing.select_one('.baths-class').text.strip()
        sqft = listing.select_one('.sqft-class').text.strip()
        listing_url = listing.select_one('a')['href']
        
        listings.append({
            'address': address,
            'city': city,
            'price': price,
            'beds': beds,
            'baths': baths,
            'sqft': sqft,
            'url': listing_url
        })
    return listings


def scrape_zillow(driver, url):
    driver.get(url)
    time.sleep(3)  # Wait for the page to load
    
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    listings = []
    for listing in soup.select('.zillow-listing-class'):  # Adjust the class to match the site
        address = listing.select_one('.zillow-address-class').text.strip()
        city = listing.select_one('.zillow-city-class').text.strip()
        price = listing.select_one('.zillow-price-class').text.strip()
        beds = listing.select_one('.zillow-beds-class').text.strip()
        baths = listing.select_one('.zillow-baths-class').text.strip()
        sqft = listing.select_one('.zillow-sqft-class').text.strip()
        listing_url = listing.select_one('a')['href']
        
        listings.append({
            'address': address,
            'city': city,
            'price': price,
            'beds': beds,
            'baths': baths,
            'sqft': sqft,
            'url': listing_url
        })
    return listings

def scrape_Apartments(driver, url):
    driver.get(url)
    time.sleep(3)  # Wait for the page to load
    
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    listings = []
    for listing in soup.select('.listing-class'):  # Adjust the class to match the site
        address = listing.select_one('.address-class').text.strip()
        city = listing.select_one('.city-class').text.strip()
        price = listing.select_one('.price-class').text.strip()
        beds = listing.select_one('.beds-class').text.strip()
        baths = listing.select_one('.baths-class').text.strip()
        sqft = listing.select_one('.sqft-class').text.strip()
        listing_url = listing.select_one('a')['href']
        
        listings.append({
            'address': address,
            'city': city,
            'price': price,
            'beds': beds,
            'baths': baths,
            'sqft': sqft,
            'url': listing_url
        })
    return listings

def scrape_Remax (driver, url):
    driver.get(url)
    time.sleep(3)  # Wait for the page to load
    
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    listings = []
    for listing in soup.select('.listing-class'):  # Adjust the class to match the site
        address = listing.select_one('.address-class').text.strip()
        city = listing.select_one('.city-class').text.strip()
        price = listing.select_one('.price-class').text.strip()
        beds = listing.select_one('.beds-class').text.strip()
        baths = listing.select_one('.baths-class').text.strip()
        sqft = listing.select_one('.sqft-class').text.strip()
        listing_url = listing.select_one('a')['href']
        
        listings.append({
            'address': address,
            'city': city,
            'price': price,
            'beds': beds,
            'baths': baths,
            'sqft': sqft,
            'url': listing_url
        })
    return listings

def scrape_HomeFinder(driver, url):
    driver.get(url)
    time.sleep(3)  # Wait for the page to load
    
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    listings = []
    for listing in soup.select('.listing-class'):  # Adjust the class to match the site
        address = listing.select_one('.address-class').text.strip()
        city = listing.select_one('.city-class').text.strip()
        price = listing.select_one('.price-class').text.strip()
        beds = listing.select_one('.beds-class').text.strip()
        baths = listing.select_one('.baths-class').text.strip()
        sqft = listing.select_one('.sqft-class').text.strip()
        listing_url = listing.select_one('a')['href']
        
        listings.append({
            'address': address,
            'city': city,
            'price': price,
            'beds': beds,
            'baths': baths,
            'sqft': sqft,
            'url': listing_url
        })
    return listings

def scrape_LoopNet(driver, url):
    driver.get(url)
    time.sleep(3)  # Wait for the page to load
    
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    listings = []
    for listing in soup.select('.listing-class'):  # Adjust the class to match the site
        address = listing.select_one('.address-class').text.strip()
        city = listing.select_one('.city-class').text.strip()
        price = listing.select_one('.price-class').text.strip()
        beds = listing.select_one('.beds-class').text.strip()
        baths = listing.select_one('.baths-class').text.strip()
        sqft = listing.select_one('.sqft-class').text.strip()
        listing_url = listing.select_one('a')['href']
        
        listings.append({
            'address': address,
            'city': city,
            'price': price,
            'beds': beds,
            'baths': baths,
            'sqft': sqft,
            'url': listing_url
        })
    return listings

def scrape_OLX(driver, url):
    driver.get(url)
    time.sleep(3)  # Wait for the page to load
    
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    listings = []
    for listing in soup.select('.listing-class'):  # Adjust the class to match the site
        address = listing.select_one('.address-class').text.strip()
        city = listing.select_one('.city-class').text.strip()
        price = listing.select_one('.price-class').text.strip()
        beds = listing.select_one('.beds-class').text.strip()
        baths = listing.select_one('.baths-class').text.strip()
        sqft = listing.select_one('.sqft-class').text.strip()
        listing_url = listing.select_one('a')['href']
        
        listings.append({
            'address': address,
            'city': city,
            'price': price,
            'beds': beds,
            'baths': baths,
            'sqft': sqft,
            'url': listing_url
        })
    return listings


def scrape_MagicBricks(driver, url):
    driver.get(url)
    time.sleep(3)  # Wait for the page to load
    
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    listings = []
    for listing in soup.select('.listing-class'):  # Adjust the class to match the site
        address = listing.select_one('.address-class').text.strip()
        city = listing.select_one('.city-class').text.strip()
        price = listing.select_one('.price-class').text.strip()
        beds = listing.select_one('.beds-class').text.strip()
        baths = listing.select_one('.baths-class').text.strip()
        sqft = listing.select_one('.sqft-class').text.strip()
        listing_url = listing.select_one('a')['href']
        
        listings.append({
            'address': address,
            'city': city,
            'price': price,
            'beds': beds,
            'baths': baths,
            'sqft': sqft,
            'url': listing_url
        })
    return listings

def scrape_Housing (driver, url):
    driver.get(url)
    time.sleep(3)  # Wait for the page to load
    
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    listings = []
    for listing in soup.select('.listing-class'):  # Adjust the class to match the site
        address = listing.select_one('.address-class').text.strip()
        city = listing.select_one('.city-class').text.strip()
        price = listing.select_one('.price-class').text.strip()
        beds = listing.select_one('.beds-class').text.strip()
        baths = listing.select_one('.baths-class').text.strip()
        sqft = listing.select_one('.sqft-class').text.strip()
        listing_url = listing.select_one('a')['href']
        
        listings.append({
            'address': address,
            'city': city,
            'price': price,
            'beds': beds,
            'baths': baths,
            'sqft': sqft,
            'url': listing_url
        })
    return listings

def scrape_Makaan(driver, url):
    driver.get(url)
    time.sleep(3)  # Wait for the page to load
    
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    listings = []
    for listing in soup.select('.listing-class'):  # Adjust the class to match the site
        address = listing.select_one('.address-class').text.strip()
        city = listing.select_one('.city-class').text.strip()
        price = listing.select_one('.price-class').text.strip()
        beds = listing.select_one('.beds-class').text.strip()
        baths = listing.select_one('.baths-class').text.strip()
        sqft = listing.select_one('.sqft-class').text.strip()
        listing_url = listing.select_one('a')['href']
        
        listings.append({
            'address': address,
            'city': city,
            'price': price,
            'beds': beds,
            'baths': baths,
            'sqft': sqft,
            'url': listing_url
        })
    return listings

def scrape_NoBroker(driver, url):
    driver.get(url)
    time.sleep(3)  # Wait for the page to load
    
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    listings = []
    for listing in soup.select('.listing-class'):  # Adjust the class to match the site
        address = listing.select_one('.address-class').text.strip()
        city = listing.select_one('.city-class').text.strip()
        price = listing.select_one('.price-class').text.strip()
        beds = listing.select_one('.beds-class').text.strip()
        baths = listing.select_one('.baths-class').text.strip()
        sqft = listing.select_one('.sqft-class').text.strip()
        listing_url = listing.select_one('a')['href']
        
        listings.append({
            'address': address,
            'city': city,
            'price': price,
            'beds': beds,
            'baths': baths,
            'sqft': sqft,
            'url': listing_url
        })
    return listings

def scrape_Trovit(driver, url):
    driver.get(url)
    time.sleep(3)  # Wait for the page to load
    
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    listings = []
    for listing in soup.select('.listing-class'):  # Adjust the class to match the site
        address = listing.select_one('.address-class').text.strip()
        city = listing.select_one('.city-class').text.strip()
        price = listing.select_one('.price-class').text.strip()
        beds = listing.select_one('.beds-class').text.strip()
        baths = listing.select_one('.baths-class').text.strip()
        sqft = listing.select_one('.sqft-class').text.strip()
        listing_url = listing.select_one('a')['href']
        
        listings.append({
            'address': address,
            'city': city,
            'price': price,
            'beds': beds,
            'baths': baths,
            'sqft': sqft,
            'url': listing_url
        })
    return listings

def scrape_Nestoria(driver, url):
    driver.get(url)
    time.sleep(3)  # Wait for the page to load
    
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    listings = []
    for listing in soup.select('.listing-class'):  # Adjust the class to match the site
        address = listing.select_one('.address-class').text.strip()
        city = listing.select_one('.city-class').text.strip()
        price = listing.select_one('.price-class').text.strip()
        beds = listing.select_one('.beds-class').text.strip()
        baths = listing.select_one('.baths-class').text.strip()
        sqft = listing.select_one('.sqft-class').text.strip()
        listing_url = listing.select_one('a')['href']
        
        listings.append({
            'address': address,
            'city': city,
            'price': price,
            'beds': beds,
            'baths': baths,
            'sqft': sqft,
            'url': listing_url
        })
    return listings

def scrape_Mitula (driver, url):
    driver.get(url)
    time.sleep(3)  # Wait for the page to load
    
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    listings = []
    for listing in soup.select('.listing-class'):  # Adjust the class to match the site
        address = listing.select_one('.address-class').text.strip()
        city = listing.select_one('.city-class').text.strip()
        price = listing.select_one('.price-class').text.strip()
        beds = listing.select_one('.beds-class').text.strip()
        baths = listing.select_one('.baths-class').text.strip()
        sqft = listing.select_one('.sqft-class').text.strip()
        listing_url = listing.select_one('a')['href']
        
        listings.append({
            'address': address,
            'city': city,
            'price': price,
            'beds': beds,
            'baths': baths,
            'sqft': sqft,
            'url': listing_url
        })
    return listings

def scrape_Hotpads(driver, url):
    driver.get(url)
    time.sleep(3)  # Wait for the page to load
    
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    listings = []
    for listing in soup.select('.listing-class'):  # Adjust the class to match the site
        address = listing.select_one('.address-class').text.strip()
        city = listing.select_one('.city-class').text.strip()
        price = listing.select_one('.price-class').text.strip()
        beds = listing.select_one('.beds-class').text.strip()
        baths = listing.select_one('.baths-class').text.strip()
        sqft = listing.select_one('.sqft-class').text.strip()
        listing_url = listing.select_one('a')['href']
        
        listings.append({
            'address': address,
            'city': city,
            'price': price,
            'beds': beds,
            'baths': baths,
            'sqft': sqft,
            'url': listing_url
        })
    return listings

def scrape_Movoto(driver, url):
    driver.get(url)
    time.sleep(3)  # Wait for the page to load
    
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    listings = []
    for listing in soup.select('.listing-class'):  # Adjust the class to match the site
        address = listing.select_one('.address-class').text.strip()
        city = listing.select_one('.city-class').text.strip()
        price = listing.select_one('.price-class').text.strip()
        beds = listing.select_one('.beds-class').text.strip()
        baths = listing.select_one('.baths-class').text.strip()
        sqft = listing.select_one('.sqft-class').text.strip()
        listing_url = listing.select_one('a')['href']
        
        listings.append({
            'address': address,
            'city': city,
            'price': price,
            'beds': beds,
            'baths': baths,
            'sqft': sqft,
            'url': listing_url
        })
    return listings

def scrape_Centris (driver, url):
    driver.get(url)
    time.sleep(3)  # Wait for the page to load
    
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    listings = []
    for listing in soup.select('.listing-class'):  # Adjust the class to match the site
        address = listing.select_one('.address-class').text.strip()
        city = listing.select_one('.city-class').text.strip()
        price = listing.select_one('.price-class').text.strip()
        beds = listing.select_one('.beds-class').text.strip()
        baths = listing.select_one('.baths-class').text.strip()
        sqft = listing.select_one('.sqft-class').text.strip()
        listing_url = listing.select_one('a')['href']
        
        listings.append({
            'address': address,
            'city': city,
            'price': price,
            'beds': beds,
            'baths': baths,
            'sqft': sqft,
            'url': listing_url
        })
    return listings

def scrape_Zoopla(driver, url):
    driver.get(url)
    time.sleep(3)  # Wait for the page to load
    
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    listings = []
    for listing in soup.select('.listing-class'):  # Adjust the class to match the site
        address = listing.select_one('.address-class').text.strip()
        city = listing.select_one('.city-class').text.strip()
        price = listing.select_one('.price-class').text.strip()
        beds = listing.select_one('.beds-class').text.strip()
        baths = listing.select_one('.baths-class').text.strip()
        sqft = listing.select_one('.sqft-class').text.strip()
        listing_url = listing.select_one('a')['href']
        
        listings.append({
            'address': address,
            'city': city,
            'price': price,
            'beds': beds,
            'baths': baths,
            'sqft': sqft,
            'url': listing_url
        })
    return listings

def scrape_Rightmove(driver, url):
    driver.get(url)
    time.sleep(3)  # Wait for the page to load
    
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    listings = []
    for listing in soup.select('.listing-class'):  # Adjust the class to match the site
        address = listing.select_one('.address-class').text.strip()
        city = listing.select_one('.city-class').text.strip()
        price = listing.select_one('.price-class').text.strip()
        beds = listing.select_one('.beds-class').text.strip()
        baths = listing.select_one('.baths-class').text.strip()
        sqft = listing.select_one('.sqft-class').text.strip()
        listing_url = listing.select_one('a')['href']
        
        listings.append({
            'address': address,
            'city': city,
            'price': price,
            'beds': beds,
            'baths': baths,
            'sqft': sqft,
            'url': listing_url
        })
    return listings

def scrape_Realestate(driver, url):
    driver.get(url)
    time.sleep(3)  # Wait for the page to load
    
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    listings = []
    for listing in soup.select('.listing-class'):  # Adjust the class to match the site
        address = listing.select_one('.address-class').text.strip()
        city = listing.select_one('.city-class').text.strip()
        price = listing.select_one('.price-class').text.strip()
        beds = listing.select_one('.beds-class').text.strip()
        baths = listing.select_one('.baths-class').text.strip()
        sqft = listing.select_one('.sqft-class').text.strip()
        listing_url = listing.select_one('a')['href']
        
        listings.append({
            'address': address,
            'city': city,
            'price': price,
            'beds': beds,
            'baths': baths,
            'sqft': sqft,
            'url': listing_url
        })
    return listings

def scrape_RealestateIndia(driver, url):
    driver.get(url)
    time.sleep(3)  # Wait for the page to load
    
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    listings = []
    for listing in soup.select('.listing-class'):  # Adjust the class to match the site
        address = listing.select_one('.address-class').text.strip()
        city = listing.select_one('.city-class').text.strip()
        price = listing.select_one('.price-class').text.strip()
        beds = listing.select_one('.beds-class').text.strip()
        baths = listing.select_one('.baths-class').text.strip()
        sqft = listing.select_one('.sqft-class').text.strip()
        listing_url = listing.select_one('a')['href']
        
        listings.append({
            'address': address,
            'city': city,
            'price': price,
            'beds': beds,
            'baths': baths,
            'sqft': sqft,
            'url': listing_url
        })
    return listings

def scrape_Savills(driver, url):
    driver.get(url)
    time.sleep(3)  # Wait for the page to load
    
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    listings = []
    for listing in soup.select('.listing-class'):  # Adjust the class to match the site
        address = listing.select_one('.address-class').text.strip()
        city = listing.select_one('.city-class').text.strip()
        price = listing.select_one('.price-class').text.strip()
        beds = listing.select_one('.beds-class').text.strip()
        baths = listing.select_one('.baths-class').text.strip()
        sqft = listing.select_one('.sqft-class').text.strip()
        listing_url = listing.select_one('a')['href']
        
        listings.append({
            'address': address,
            'city': city,
            'price': price,
            'beds': beds,
            'baths': baths,
            'sqft': sqft,
            'url': listing_url
        })
    return listings

def scrape_Bing(driver, url):
    driver.get(url)
    time.sleep(3)  # Wait for the page to load
    
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    listings = []
    for listing in soup.select('.listing-class'):  # Adjust the class to match the site
        address = listing.select_one('.address-class').text.strip()
        city = listing.select_one('.city-class').text.strip()
        price = listing.select_one('.price-class').text.strip()
        beds = listing.select_one('.beds-class').text.strip()
        baths = listing.select_one('.baths-class').text.strip()
        sqft = listing.select_one('.sqft-class').text.strip()
        listing_url = listing.select_one('a')['href']
        
        listings.append({
            'address': address,
            'city': city,
            'price': price,
            'beds': beds,
            'baths': baths,
            'sqft': sqft,
            'url': listing_url
        })
    return listings



# Function to handle pagination and scrape all pages
def scrape_all_pages(driver, base_url, scrape_function):
    all_listings = []
    page = 1
    while True:
        url = f"{base_url}&page={page}"
        listings = scrape_function(driver, url)
        if not listings:
            break
        all_listings.extend(listings)
        page += 1
    return all_listings

# Main function to orchestrate scraping
def main():
    driver = init_driver()
    
    all_data = []

    # Example URLs (replace with actual URLs)
    vestapreferred_url = "https://vestapreferred.com/listings"
    zillow_url = "https://www.zillow.com/homes/for_sale/"
    Redfin_url = " https://www.redfin.com/"
    Trulia_url = " https://www.trulia.com/"
    Point2Homes_url = " https://www.point2homes.com/"
    Zillow_url = " https://www.zillow.com/"
    Apartments_url = "https://www.apartments.com/"
    Remax_url = " https://www.remax.com/"
    HomeFinder_url = " https://homefinder.com/"
    LoopNet_url = "https://www.loopnet.com/"
    OLX_url = "https://www.olx.in/"
    MagicBricks_url = "https://www.magicbricks.com/"
    Housing_url =" https://housing.com/"
    Makaan_url = " https://www.makaan.com/"
    NoBroker_url = " https://www.nobroker.in/"
    Trovit_url = "https://property.trovit.co.in/"
    Quikr_url = "https://www.quikr.com/homes"
    Nestoria_url = " https://www.nestoria.in/"
    Mitula_url = "https://property.mitula.in/"
    Hotpads_url = " https://hotpads.com/"
    Movoto_url = " https://www.movoto.com/"
    Centris_url = "https://www.centris.ca/en"
    Zoopla_url = "https://www.zoopla.co.uk/"
    Rightmove_url = " https://www.rightmove.co.uk/"
    Realestate_url = " https://www.realestate.com.au/"
    RealestateIndia_url = "https://www.realestateindia.com/"
    Savills_url = " https://www.savills.com/"
    Bing_url = " https://www.bing.com/homes?setlang=en-US"

    
    # Scrape data from Vesta Preferred Realty
    vestapreferred_listings = scrape_all_pages(driver, vestapreferred_url, scrape_vestapreferred)
    all_data.extend(vestapreferred_listings)
    
    # Scrape data from Zillow
    zillow_listings = scrape_all_pages(driver, zillow_url, scrape_zillow)
    all_data.extend(zillow_listings)
    
    # Convert to DataFrame and save as CSV
    df = pd.DataFrame(all_data)
    df.to_csv('real_estate_listings.csv', index=False)
    
    driver.quit()

if __name__ == "__main__":
    main()


# In[22]:


import requests
from bs4 import BeautifulSoup
import pandas as pd

# Example function to scrape a single page
def scrape_vestapreferred_page(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    listings = []
    for listing in soup.select('.listing-class'):  # Adjust the class to match the site
        address = listing.select_one('.address-class').text
        city = listing.select_one('.city-class').text
        price = listing.select_one('.price-class').text
        beds = listing.select_one('.beds-class').text
        baths = listing.select_one('.baths-class').text
        sqft = listing.select_one('.sqft-class').text
        listing_url = listing.select_one('a')['href']
        
        listings.append({
            'address': address,
            'city': city,
            'price': price,
            'beds': beds,
            'baths': baths,
            'sqft': sqft,
            'url': listing_url
        })
    
    return listings

# Example URL - adjust to the actual URL
url = 'https://vestapreferred.com/'
data = scrape_vestapreferred_page(url)

# Save to a DataFrame
df = pd.DataFrame(data)
df.to_csv('vestapreferred_listings.csv', index=False)


# In[24]:


import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pandas as pd
import time
import re


conversion_rates = {
    'USD': 83.12,
    'Euro': 90.73,
    'CHF': 95.73,
    'KWD': 270.04,
    'AED': 22.63
}


def init_driver():
    driver = webdriver.Chrome(options=options)
    return driver


def convert_to_inr(price, currency):
    if currency in conversion_rates:
        inr_price = price * conversion_rates[currency]
    else:
        inr_price = price  
    return round(inr_price)


def scrape_vestapreferred(driver, url):
    driver.get(url)
    time.sleep(3)  
    
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    listings = []
    for listing in soup.select('.listing-class'):  # Adjust the class to match the site
        address = listing.select_one('.address-class').text.strip() if listing.select_one('.address-class') else None
        city = listing.select_one('.city-class').text.strip() if listing.select_one('.city-class') else None
        price_text = listing.select_one('.price-class').text.strip() if listing.select_one('.price-class') else None
        beds = listing.select_one('.beds-class').text.strip() if listing.select_one('.beds-class') else None
        baths = listing.select_one('.baths-class').text.strip() if listing.select_one('.baths-class') else None
        sqft_text = listing.select_one('.sqft-class').text.strip() if listing.select_one('.sqft-class') else None
        listing_url = listing.select_one('a')['href'] if listing.select_one('a') else None
        
        
        if price_text:
            price_match = re.match(r'(\d+(?:,\d+)*)\s*(\w+)', price_text)
            if price_match:
                price = float(price_match.group(1).replace(',', ''))
                currency = price_match.group(2)
                price = convert_to_inr(price, currency)
            else:
                price = None
        else:
            price = None
        
        
        if sqft_text:
            sqft_match = re.match(r'(\d+(?:,\d+)*)\s*(\w+)', sqft_text)
            if sqft_match:
                sqft = float(sqft_match.group(1).replace(',', ''))
                unit = sqft_match.group(2)
                if unit.lower() in ['sqm', 'm2', 'square meters']:
                    sqft *= 10.7639 
            else:
                sqft = None
        else:
            sqft = None
        
        listings.append({
            'address': address,
            'city': city,
            'price': price,
            'beds': beds,
            'baths': baths,
            'sqft': sqft,
            'url': listing_url
        })
    
    return listings


def scrape_all_pages(driver, base_url, scrape_function):
    all_listings = []
    page = 1
    while True:
        url = f"{base_url}&page={page}"
        listings = scrape_function(driver, url)
        if not listings:
            break
        all_listings.extend(listings)
        page += 1
    return all_listings


def main():
    driver = init_driver()
    
    all_data = []

    
    vestapreferred_url = "https://vestapreferred.com/"
    
    
    vestapreferred_listings = scrape_all_pages(driver, vestapreferred_url, scrape_vestapreferred)
    all_data.extend(vestapreferred_listings)
    
    
    df = pd.DataFrame(all_data)
    
    df['address'].fillna('Unknown Address', inplace=True)
    df['city'].fillna('Unknown City', inplace=True)
    df['beds'].fillna('0', inplace=True)
    df['baths'].fillna('0', inplace=True)
    df['sqft'].fillna(df['sqft'].mean(), inplace=True)  
    
    
    df.to_csv('real_estate_listings.csv', index=False)
    
    driver.quit()


    


# In[3]:


def convert_to_inr(price, currency):
    if currency in conversion_rates:
        return round(price * conversion_rates[currency])
    else:
        
        return round(price)


# In[7]:


def scrape_vesta_preferred_realty():
    base_url = "https://vestapreferred.com/"
    data = []
    
    return data


# In[8]:


def scrape_trulia():
    base_url = "https://www.trulia.com/"
    data = []
    
    return data


# In[9]:


def scrape_homes():
    base_url = "https://www.homes.com/"
    data = []
 
    return data


# In[10]:


def scrape_realtor():
    base_url = "https://www.realtor.com/"
    data = []
    
    return data


# In[11]:


def scrape_point2homes():
    base_url = "https://www.point2homes.com/"
    data = []
    
    return data


# In[12]:


def scrape_Zillow():
    base_url = "https://www.zillow.com/"
    data = []
    
    return data


# In[13]:


def scrape_Apartments():
    base_url = " https://www.apartments.com/"
    data = []
    
    return data


# In[15]:


def scrape_HomeFinder():
    base_url = " https://homefinder.com/"
    data = []
   
    return data


# In[14]:


def scrape_LoopNet():
    base_url = " https://www.loopnet.com/"
    data = []
    
    return data


# In[16]:


def scrape_OLX():
    base_url = "https://www.olx.in/"
    data = []
    
    return data


# In[17]:


def scrape_MagicBricks():
    base_url = "https://www.magicbricks.com/"


    data = []
  
    return data


# In[18]:


def scrape_Housing():
    base_url = "https://housing.com/"


    data = []
  
    return data


# In[19]:


def scrape_Makaan():
    base_url = "https://www.makaan.com/"


    data = []
  
    return data


# In[20]:


def scrape_NoBroker():
    base_url = "https://www.nobroker.in/"


    data = []
  
    return data


# In[21]:


def scrape_Trovit():
    base_url = "https://property.trovit.co.in/"


    data = []
  
    return data


# In[22]:


def scrape_Quikr():
    base_url = "https://www.quikr.com/homes"


    data = []
  
    return data


# In[ ]:




