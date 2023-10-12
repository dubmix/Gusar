import argparse
import sys

from scraper import ListingsScraper

#parser = argparse.ArgumentParser()
#parser.add_argument("-release_id")

def main():
    if len(sys.argv) != 2:
        return
    else:
        args = sys.argv[1]
        listings = ListingsScraper().scrape(args)
        print(listings)

if __name__ == "__main__":
    main()
    print("success")
