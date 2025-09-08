# 11. Write a program anti_html.py that takes a URL as argument, downloads the html from web 
# 0and print it after stripping html tags. 

import sys
import requests
import re

url=sys.argv[1]
def strip_tage(html):
    html = re.sub(r'<(script|style).*?>.*?</\1>', '', html)
    html = re.sub(r'<[^>]+>', '', html)
    return re.sub(r'\s+', ' ', html).strip()

# with open(sys.argv[1], "r") as f:
#             html = f.read()

html=requests.get(sys.argv[1],timeout=19).text
print(strip_tage(html))
