#!/usr/bin/python3

# powered by newsapi.org

import argparse
from secret import newsapikey
from newsapi import NewsApiClient

def main() : 

   parser = argparse.ArgumentParser()
   parser.add_argument("-q", "--query", help="Search query.", dest='query')
   args = parser.parse_args()

   newsapi = NewsApiClient(api_key=newsapikey)

   # /v2/top-headlines
   #r = newsapi.get_top_headlines(q=args.query, language='en')
   #print(r)

   r = newsapi.get_sources()
   print(r)

   #newsapi.get_sources(category="technology")
   #newsapi.get_sources(country="us")
   #newsapi.get_sources(category="health", country="us")
   #newsapi.get_sources(language="en", country="in")

if __name__ == "__main__" : 
    main()
