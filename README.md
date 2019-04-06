# Django app & Scrapy

## 1: Initial Setup

#### Clone project in a new directory:
```bash
cd path/to/a/new/directory
git clone https://github.com/MaksNech/pylab2018_ht_22.git
```


## 2: Getting Started
#### Start backend:
Inside project create virtual environment:
```bash
virtualenv -p python3 env
```
Then start virtual environment:
```bash
source env/bin/activate
```
Install packages using pip according to the requirements.txt file:
```bash
pip install -r requirements.txt
```
Inside project directory run app with terminal command:
```bash
python3 manage.py runserver
```
#### Admin:
##### Username: admin
##### Email address: admin@mail.com
##### Password: 123

#### Start Scraping data:
Inside project directory run celery and scrapy with terminal commands:
```bash
celery -A store worker -l info

scrapy crawl net_a_porter_bags
```
Then go to the site in browser and press 'scrapping' button.

#### Clear Redis:
enter to Redis:
```bash
redis-cli
```
clear all databases:
```bash
FLUSHDB
```
show keys in Redis:
```bash
keys *
```
