from flask import Blueprint, render_template, request
from config import Config
import os
import json
import urllib.request
import pandas as pd

weather_bp = Blueprint("weather_bp", __name__, template_folder="templates")
cities_list = os.path.join(
    os.path.dirname(__file__), "static", "weather_cities", "cities_list.xlsx"
)


@weather_bp.route("/", methods=["POST", "GET"])
def weather():
    weather_cities = pd.read_excel(cities_list).name.values
    city = "Hanoi"

    if request.method == "POST" and request.form["city"].capitalize() in weather_cities:
        city = request.form["city"].capitalize()

    weather_api = Config.WEATHER_API_KEY
    source = urllib.request.urlopen(
        "https://api.openweathermap.org/data/2.5/weather?q="
        + city
        + "&appid="
        + weather_api
    ).read()
    list_data = json.loads(source)
    temp_k = list_data["main"]["temp"]
    coord_lon = list_data["coord"]["lon"]
    coord_lat = list_data["coord"]["lat"]

    data = {
        "cityname": list_data["name"],
        "country_code": list_data["sys"]["country"],
        "coordinate": f"{round(coord_lon, 2)}, {round(coord_lat,2)}",
        "temp_cel": f"{int(temp_k - 273.15)}",
        "temp": temp_k,
        "pressure": list_data["main"]["pressure"],
        "humidity": list_data["main"]["humidity"],
    }
    return render_template("index.html", data=data)
