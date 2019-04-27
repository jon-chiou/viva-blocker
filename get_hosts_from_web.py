#! usr/bin/benv python3

"""This script grabs a list of known obnoxious urls, parses the text for just the urls,
 then formats them for Chromium extensions as a .js array with wildcards"""

import requests
import re

url = "https://raw.githubusercontent.com/StevenBlack/hosts/master/hosts"

response = requests.get(url)

url_line_pattern = re.compile(r"^0\.0\.0\.0 .*")


def format_urls(response_text):
    with open("blocked_domains.js","w") as blacklist_file:
        blacklist_file.write("var blocked_domains = [\n")
        for text in response_text:
            match_url = url_line_pattern.match(text)
            if match_url is not None:
                match_string = match_url.group(0)
                new_url = match_string.split(" ")
                formatted_url = "\"*://*." + new_url[1] + "/*\",\n"
                blacklist_file.write(formatted_url)
        blacklist_file.write("];")
        blacklist_file.close()


format_urls(response.text.splitlines())

__author__ = "Jonathan Chiou"
