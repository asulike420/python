
"""
   Install Dependencies: Ensure you have the necessary libraries installed.
The most commonly used libraries for web scraping in Python are 
requests, beautifulsoup4, and lxml. You can install them using pip:
pip install requests beautifulsoup4 lxml
"""

import requests
from bs4 import BeautifulSoup

"""
Send HTTP Request: Use the requests library to 
send an HTTP GET request to the target web page and retrieve the HTML content:
"""
url = "https://en.wikipedia.org/wiki/India"  # Replace with the target URL
response = requests.get(url)
html_content = response.text

"""
Parse HTML: Use the BeautifulSoup
 library to parse the HTML content and create a BeautifulSoup object:
"""
soup = BeautifulSoup(html_content, 'lxml')

"""
Extract Data: Use BeautifulSoup's methods to 
locate and extract the desired data from the HTML structure. 
You can find elements by their tag name, class, id, or other attributes:
"""

# Example: Extract all links from the page
links = soup.find_all('a')                                                                                                                                                                                                  E
for link in links:
    print(link['href'])

