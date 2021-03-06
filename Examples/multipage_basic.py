#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from GoogleScraper import scrape_with_config, GoogleSearchError

# See in the config.cfg file for possible values
config = {
    'use_own_ip': True,
    'keyword': '如何打酱油',
    'search_engines': ['bing','baidu','google'],
    'num_pages_for_keyword': 2,
    'scrape_method': 'http',
    'no_caching': True,
}

try:
    search = scrape_with_config(config)
except GoogleSearchError as e:
    print(e)

# let's inspect what we got
for serp in search.serps:
    # print(serp)
    # print(serp.search_engine_name)
    # print(serp.scrape_method)
    # print(serp.page_number)
    # print(serp.requested_at)
    # print(serp.num_results)
    # ... more attributes ...
    for link in serp.links:
        print(link.domain,link.title,link.visible_link,link.link,link.snippet)
