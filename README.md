# Yivo_Search

## Introduction
Yivo Search is a tool developed to provide quick analysis of URLs against multiple Open Source Intelligence feeds. Results are stored in a SQlite database and displayed when queried. Current sources include URLScan.io, URLHaus, Google Safe Search API, OpenPhish Feed, Phishtank, Virustotal, and McAfee Web Advisor. I hope to include additional modules in the near future.

## Setup
1. Clone or download the repository keeping the observed directory structure then run pip.
2. pip install -r requirements.txt
3. Setup the sqlite DB. 

Schema statement
CREATE TABLE "results" (
	"created_time"	TEXT,
	"value"	TEXT,
	"engine_urlscan"	TEXT,
	"engine_googlesafe"	TEXT,
	"engine_webadvisor"	TEXT,
	"engine_phishtank"	TEXT,
	"engine_virustotal"	TEXT,
	"engine_openphish"	TEXT
)

4. Edit this line of the yivosearch.py to reflect your db name. db_path = os.path.join(BASE_DIR, "yivohunt.db")

### Modules
As described above their are currently 7 different modules to query URLs against. Please be sure to observe limitations these services place on volume of querying against the APIs in some cases.

#### VirusTotal
Obtain VT API access
https://developers.virustotal.com/reference#getting-started

Append to the config.conf

#### OpenPhish

OpenPhish Community only offers downloading of the IOCs via text file and are updated every 12 hours. You can create a simple wget or curl script to run as a cronjob to pull the IOCs.

https://openphish.com/feed.txt

The file should be in the main directory or update the location referenced in the openphish module.

#### AbuseCH

Like the OpenPhish feed Abuse.ch URLHaus offers an option to download a text only list of URLs so no API key is required.  You'll also need to use a script to pull these regularly.

https://urlhaus.abuse.ch/api/

#### URLScan.io

URLScan API information
https://urlscan.io/about-api/#search

#### Phishtank

Phishtank feed offers an API that you'll need to append to the config file.
https://www.phishtank.com/api_register.php

The module parses the data from .json format for matching.

#### Google Safe Search

You'll also need a Google Developer API. API information can be found here - https://developers.google.com/safe-browsing/v4

Create an API here https://console.developers.google.com/ and update the config file.

#### McAfee Web Advisor

No API needed for this. Module scrapes the HTML using BeautifulSoup. 

## Usage



## Extras
This project can easily be stripped of the SQL DB and ported to a web framework such as Django. 

![Image of Django](https://github.com/plushed/Yivo_Search/blob/master/django_screen.PNG)


