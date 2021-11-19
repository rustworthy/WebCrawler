"""Set default values of the main constants.

All of the constants are allowed to be set via commandline as its arguments.
The default values, though, are taken from here by the argparser-module."""

import os
import dotenv

dotenv.load_dotenv()

HEADERS = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                         "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36"}
WEBDRIVER_PATH = os.getenv("WEBDRIVER_PATH")
TARGET_DIR_PATH = os.getenv("TARGET_DIR_PATH")
PAGE_TO_SCRAPE = "https://www.reddit.com/top/?t=month"
POSTS_FOR_PARSING_NUM = 5

HOST = 'localhost'
PORT = 8087
SERVER_NAME = 'reddit-scraper'
