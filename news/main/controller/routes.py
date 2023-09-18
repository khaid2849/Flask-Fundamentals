import os
from flask import Blueprint, request, render_template

from news.main.service.news import get_all_articles, get_all_headlines


news_bp = Blueprint("news_bp", __name__, template_folder="../templates")
templates_dir = os.path.join(os.path.dirname(__file__), "templates")


@news_bp.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        keyword = request.form["keyword"]
        all_articles = get_all_articles(keyword)
        return render_template("home.html", all_articles=all_articles, keyword=keyword)
    else:
        all_headlines = get_all_headlines()
        return render_template("home.html", all_headlines=all_headlines)
