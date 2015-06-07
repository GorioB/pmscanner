# pmscanner
Philmusic.com guitar classifieds scraper

Scrapes the Guitar Classifieds Forum by trying to match guitar brands and models.

Usage
-----

    scrapy crawl guitars -a model=<FILTER_MODEL> -a pages=<# PAGES> -a brand=<FILTER_BRAND> -a status=<FILTER STATUS>

Generates an HTML file `output.html` with gathered information and images. Also generates a JSON file, `output.json`.

A list of supported guitar brands and models can be updated in `guitartypes.py`.

Can filter by `brand`, `model`, or sale `status` (For Sale, For Trade, or Sold) using the respective argument.

By default, only retrieves one forum page (around 50 postings); use `pages` argument to specify more pages.
