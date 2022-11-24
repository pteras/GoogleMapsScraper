from flask import Flask, request
import json
from scraper import get_data
from flask_cors import CORS
import requests


api = Flask(__name__)
CORS().init_app(api)

# get POST request body
@api.route("/api/scraper", methods=["POST"])
def fetch_data():
    data = request.get_json()
    address = data["address"]
    business_type = data["businessType"]
    radius = data["radius"]
    return get_data(address, business_type, radius)


if __name__ == "__main__":
    api.run()


    
    