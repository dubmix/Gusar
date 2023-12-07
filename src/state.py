import json
from logging import Logger
from logger import logger

def read_state(path: str, logger: Logger = logger) -> dict:
    logger.info(f"Reading state from {path}")
    try:
        with open(path, "r") as fh:
            state = json.load(fh)
        logger.debug("State file found")
    except FileNotFoundError:
        logger.debug(f"State file not found")
        state = {}
    return state

def write_state(state: dict, path: str, logger: Logger = logger) -> None:
    logger.info(f"Writing state to {path}")
    with open(path, "w+") as fh:
        json.dump(state, fh)