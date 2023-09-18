from news.config import Config

import json
import urllib
import pycountry
import os


def get_news_api(
    q=None,
    country=None,
    page_size=None,
    language="en",
):
    api_key = Config.NEWS_API_KEY
    url = f"https://newsdata.io/api/1/news?apikey={api_key}&language={language}"
    if q:
        url = url + f"&q={q}"
    if country:
        url = url + f"&country={country}"
    if page_size:
        url = url + f"&size={page_size}"

    source = urllib.request.urlopen(
        "https://newsdata.io/api/1/news?apikey=" + api_key
    ).read()
    list_data = json.loads(source)
    return list_data


def get_current_country():
    f = open("news/static/countries.json")
    contries_obj = json.load(f)

    country_code = ""
    url = "http://ipinfo.io/json"
    response = urllib.request.urlopen(url)
    data = json.load(response)

    current_country_name = pycountry.countries.get(
        alpha_2=data.get("country")
    ).common_name
    if current_country_name in contries_obj:
        country_code = contries_obj[current_country_name]

    return country_code


def get_all_headlines():
    country_code = get_current_country()
    top_headlines = get_news_api(country=country_code)
    total_results = (
        25 if top_headlines["totalResults"] > 25 else top_headlines["totalResults"]
    )

    all_headlines = get_news_api(country=country_code, page_size=total_results)[
        "results"
    ]

    return all_headlines


def get_all_articles(keyword):
    country_code = get_current_country()
    news_by_keyword = get_news_api(country=country_code, q=keyword, page_size=25)

    return news_by_keyword["results"]
