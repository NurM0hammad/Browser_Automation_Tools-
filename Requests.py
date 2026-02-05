import requests
from bs4 import BeautifulSoup

# Get page content
response = requests.get('https://nimble-kitten-2445a2.netlify.app/')
soup = BeautifulSoup(response.content, 'html.parser')

# Parse data
title = soup.find('h1').text
links = [a['href'] for a in soup.find_all('a', href=True)]