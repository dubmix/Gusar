from logger import logger

def get_new_listing_ids(current_ids, old_ids, logger=logger):
    #compares current and old listings IDs
    #updates the list if necessary
    if current_ids:
        new_ids = list(set(current_ids) - set(old_ids))
    else:
        logger.info("No current IDs found") 
        new_ids = []
    logger.info(f"Found {len(new_ids)} new items in the wantlist")
    return new_ids