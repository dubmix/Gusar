from typing import List

import requests
from bs4 import BeautifulSoup
from bs4.element import ResultSet

class ListingsScraper:
    def __init__(self):
        self.base_url = "https://discogs.com/release/"
    
    def get_listings_soup(self, release_id: int) -> ResultSet:
        headers = {"User-Agent": "friendly"}
        response = requests.get(f"{self.base_url}{release_id}", headers=headers)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")
        return soup.find_all("tr")

    def parse_listing(self, listing: ResultSet) -> dict:
        label = listing.find("a", {})
        return {
            "Label": label,
            "Format": frmt,
        }
    
    def scrape(self, release_id: int):
        listings = []
        soup_listings = self.get_listings_soup(release_id)
        for listing in soup_listings:
            listings.append(listing)
        return listings