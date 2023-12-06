import os
import sys

from scraper import ListingsScraper
#from state import read_state, write_state
from logger import logger
#from helper import get_new_listing_ids

RELEASE_IDS = ["631068",]

def main():
    '''
    if len(sys.argv) != 2:
        return
    else:
        args = sys.argv[1]
        listings = ListingsScraper().scrape(args)
    '''
    logger.info(f"Scanning {len(RELEASE_IDS)} releases")
    for release_id in RELEASE_IDS:
        print(f"release_id: {release_id}")
        current_listings = ListingsScraper().scrape(release_id)
    for entry in current_listings:
        print("\n", entry["title"])
        print(entry["href"])
        print(entry["id"])
        print(entry["media_condition"])
        print(entry["sleeve_condition"])
        print(entry["ships_from"])
        print(entry["price"])

if __name__ == "__main__":
    main()
