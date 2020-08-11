# Yivo_Search

## Introduction
Yivo Search is a tool developed to provide quick analysis of URLs against multiple Open Source Intelligence feeds. Results are stored in a SQlite database and displayed when queried. Current sources include URLScan.io, Google Safe Search API, OpenPhish Feed, Phishtank, Virustotal, and McAfee Web Advisor. I hope to include additional modules in the near future.

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
As described above their are currently 6 different modules to query URLs against.

#### VirusTotal
#### OpenPhish
#### AbuseCH
#### Phishtank
#### Google Safe Search
#### McAfee Web Advisor

### Configuration

## Extras
This project can easily be stripped of the SQL DB and ported to a web framework such as Django. 

![Image of Django]()


