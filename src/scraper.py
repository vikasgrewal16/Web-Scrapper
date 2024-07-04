from urllib.error import URLError
from utils import read_websites_from_csv 
import logging
from cms_detector import detect_cms
from bs4 import BeautifulSoup
import requests
import re


def fetch_page_content(url, max_retries=3, backoff_factor=2, max_wait_time=30):
    """Fetches webpage content with retry logic and backoff."""
    total_wait = 0
    retries = 0
    while retries < max_retries and total_wait < max_wait_time:
        try:
            response = requests.get(url)
            response.raise_for_status()  # Raise exception for non-200 status codes
            return response.text
        except (URLError, TimeoutError, ConnectionResetError, NameResolutionError) as e:
            error_message = f"Error fetching {url} (retry {retries+1}/{max_retries}): {str(e)}"
            log_error(error_message)
            retries += 1
            wait_time = backoff_factor ** retries
            total_wait += wait_time
            time.sleep(min(wait_time, max_wait_time - total_wait))  # Limit wait time
    else:
        # All retries failed or max wait time reached, log final error
        log_error(f"Failed to scrape {url} after {max_retries} retries.")
        return None  # Indicate failed fetch

def parse_html(html):
    """Parses HTML content using BeautifulSoup."""
    return BeautifulSoup(html, 'html.parser')

def extract_email(soup):
    """Extracts email addresses from HTML."""
    emails = re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', soup.text)
    return emails[0] if emails else None

def extract_address(soup):
    address_data = []
    ## using specific keywords
    keywords = ["street", "avenue", "road", "highway", "city", "state", "zip"]
    potential_address_elements = soup.find_all(text=lambda text: text and any(keyword in text.lower() for keyword in keywords))
    for element in potential_address_elements:
        parent = element.parent
        while parent:
            if parent.name in ["p", "div", "span"]:
                address_data.append(parent.text.strip())
                break
            parent = parent.parent

    # Return the first non-empty address or "Not found"
    return address_data[0] if address_data else "Not found"

def extract_contact_number(soup):
    """Extracts contact numbers from HTML."""
    numbers = re.findall(r'\+\d{1,3}\s?\(?\d{1,4}?\)?[\d\s-]{5,15}', soup.text)
    return numbers[0] if numbers else None

def detect_cms(soup):
    """Detects CMS using cms-detector library."""
    try:
        return detect_cms(url)  # Assuming URL is available within the function
    except Exception as e:
        log_error(f"Error detecting CMS for {url}: {str(e)}")
        return "Unknown"

def scrape_website(url):
    """Scrapes a website, extracts data, and detects CMS."""
    html_content = fetch_page_content(url)
    if not html_content:
        return  # Skip website if content fetch fails

    soup = parse_html(html_content)

    email = extract_email(soup)
    address = extract_address(soup)
    contact_number = extract_contact_number(soup)
    cms = detect_cms(soup)  # Assuming URL is accessible within the function

    # Process or store the extracted data (email, address, contact number, CMS)
    # and website category
    print(f"URL: {url}")
    print(f"Email: {email}")
    print(f"Address: {address}")
    print(f"Contact Number: {contact_number}")
    print(f"CMS: {cms}")
    print("-" * 50)
