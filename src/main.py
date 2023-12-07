import os
import sys

from scraper import ListingsScraper
from state import read_state, write_state
from logger import logger
from helpers import get_new_listing_ids

RELEASE_IDS = ["631068", "10085219"]

YELLOW = '\033[93m'
RESET_PRINT = '\033[0m'

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
        print(f"{YELLOW}Printing listings for release_id: {release_id}{RESET_PRINT}")

        # retrieving the listing for a release
        current_listings = ListingsScraper().scrape(release_id)
        
        # retrieving all listing ids for that release
        current_listing_ids = [listing["listing_id"] for listing in current_listings]

        for entry in current_listing_ids:
            print(entry)

        for entry in current_listings:
            print("\n", entry["title"])
            print(entry["href"])
            #print(entry["listing_id"])
            print(entry["media_condition"])
            print(entry["sleeve_condition"])
            print(entry["ships_from"])
            print(entry["price"])

if __name__ == "__main__":
    main()
